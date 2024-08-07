<!--
    Run pyodide in xterm.js.
    
    Code inspired from https://whitefirer.org/html/pyodide/, modified:
        - update for modern XTerm.js support
        - TypeScript
        - support more terminal features:
            - SUPPR key
            - Ctrl+arrows
            - Ctrl+L
            - Ctrl+C
        - code cleanup, greatly simplify terminal handling
        - bundle Scapy
-->

<template>
    <div id="terminal" ref="terminal"></div>
</template>

<script lang="ts">
// JS Imports
import { ref, Ref } from 'vue';
import { Terminal } from 'xterm';
import { loadPyodide } from 'pyodide';
import { startXterm, showCursor, hideCursor, disableStdin } from '@/components/XTerm.vue';

// Python variables
const pyodideIndexURL = "https://cdn.jsdelivr.net/pyodide/v0.23.4/full/";
const scapyWheelURL = new URL(`/${process.env.scapywhl}`, import.meta.url).href;

// Constants
const VK_RETURN = '\r';
const VK_CLEAR = '\u000c';
const VK_DELETE = '\u007F';
const VK_CANCEL = '\u0003';
const VK_UP = '\x1b[A';
const VK_DOWN = '\x1b[B';
const VK_RIGHT = '\x1b[C';
const VK_LEFT = '\x1b[D';
const VK_CTRL_RIGHT = '\x1b[1;5C';
const VK_CTRL_LEFT = '\x1b[1;5D';
const VK_SUPPR = '\x1b[3~';

// Terminal utils
var pythonCodeX = 0;
var pythonCodeY = 0;
var historyCodeList: string[] = [];
var lastPythonCodeLine = "";
var renderingCode = true;

// pyodide
var pyodide: any = null;

// XTerm.js
const terminal: Ref<HTMLElement | null> = ref(null); // container
const term = new Terminal(); // xterm.js object

// Python terminal
var pythonCode = '';
var historyIndex = 0;
var historyCode = "";
var lastCRIndex = 0;

export function mountFile(file: File) {
    /*
     * Mount a File
     */
    const freader = new FileReader();
    freader.addEventListener('loadend', () => {
        //@ts-ignore
        pyodide.FS.writeFile(file.name, new Uint8Array(freader.result));
        term.write(`\x1b[0m\rFile '${file.name}' was imported in the Emscripten file system !\n`);
        pythonCodeY = term.buffer.normal.cursorY + term.buffer.normal.baseY + 1;
        displayCurrentPrompt();
    });
    freader.readAsArrayBuffer(file);
}

function recalcFromPythonCode() {
    /*
     * Recalculate cursor position based on 
     */
    if (pythonCode.length === 0) {
        pythonCodeX = term.buffer.normal.cursorX + 1;
        pythonCodeY = term.buffer.normal.cursorY + term.buffer.normal.baseY + 1;
    }
    let currentCursorY = term.buffer.normal.cursorY + term.buffer.normal.baseY + 1;
    lastCRIndex = pythonCode.lastIndexOf('\r');
    let lastEditIndex = term.buffer.normal.cursorX - 4;
    let editIndex = lastEditIndex;
    lastPythonCodeLine = pythonCode.substring(lastCRIndex + 1, pythonCode.length + 1);
    if (lastPythonCodeLine.length >= term.cols - 4) {
        editIndex = lastEditIndex + (currentCursorY - pythonCodeY) * term.cols;
    }
    return { currentCursorY, lastEditIndex, editIndex };
}

function prompt() {
    /*
     * Display xterm.js prompt
     */
    term.write('\r\x1b[34m>>> ');
};

function setCursorPosition(x: Number, y: Number) {
    /*
     * Set the cursor position in the terminal
     */
    term.write(`\x1b[${y};${x}H`)
}

async function writeHighlightPythonCode(x: Number, y: Number, pythonCode: string) {
    /*
     * Call pygments to highlight the Python input and print it into the terminal.
     */
    setCursorPosition(x, y);
    // term.write(pythonCode);
    await pyodide.runPythonAsync(`
        _PY_code = """
        ${pythonCode.replaceAll("\\", "\\\\")}
        """
        _PY_highlighted_code = highlight(_PY_code, PythonLexer(), TerminalTrueColorFormatter(style='native'));
        _PY_highlighted_code[:-1]
    `).then((output: string) => {
        term.write(output.replaceAll('\n', '\r\n... '));
    });
}

function writeByteOnTerm(data: number) {
    /*
     * Write to terminal output. Called directly by pyodide
     */
    if (data == 10) { // \n
        term.write("\r\n");
    } else {
        term.write(new Uint8Array([data]));
    }
}

function displayCurrentPrompt() {
    /*
     * Display the prompt string based on the state
     */
    if (pythonCodeY === (term.buffer.normal.cursorY + term.buffer.normal.baseY + 1)) {
        term.write('\r\x1b[2K\x1b[34m>>> ');
    } else if (term.buffer.normal.cursorX > 4) {
        term.write('\r\x1b[2K... ');
    } else {
        term.write('\r\x1b[2K');
    }
}

term.onData(e => {
    /*
     * Handling of all key presses
     */
    switch (e) {
        // handle slow navigation
        case VK_LEFT:
            if (term.buffer.normal.cursorX > 4) {
                setCursorPosition(term.buffer.normal.cursorX, term.buffer.normal.cursorY + 1);
            }
            break;
        case VK_RIGHT:
            lastCRIndex = pythonCode.lastIndexOf('\r');
            lastPythonCodeLine = pythonCode.substring(lastCRIndex + 1, pythonCode.length + 1);
            if (term.buffer.normal.cursorX < (lastPythonCodeLine.length % term.cols + 4)) {
                setCursorPosition(term.buffer.normal.cursorX + 2, term.buffer.normal.cursorY + 1);
            }
            break;
        case VK_CTRL_LEFT:
        case VK_CTRL_RIGHT:
            // handle fast navigation
            lastCRIndex = pythonCode.lastIndexOf('\r');
            lastPythonCodeLine = pythonCode.substring(lastCRIndex + 1, pythonCode.length + 1);
            let spaceIndex;
            if (e == VK_CTRL_LEFT) {
                lastPythonCodeLine = " " + lastPythonCodeLine;
                lastPythonCodeLine = lastPythonCodeLine.slice(0, term.buffer.normal.cursorX - 4);
                if (lastPythonCodeLine.endsWith(" "))
                    lastPythonCodeLine = lastPythonCodeLine.slice(0, -1);
                spaceIndex = lastPythonCodeLine.lastIndexOf(" ");
                if (spaceIndex != -1)
                    spaceIndex += 1;
            } else {
                lastPythonCodeLine = lastPythonCodeLine + " ";
                lastPythonCodeLine = lastPythonCodeLine.slice(term.buffer.normal.cursorX - 3);
                if (lastPythonCodeLine.startsWith(" "))
                    lastPythonCodeLine = "_" + lastPythonCodeLine.slice(1);
                spaceIndex = lastPythonCodeLine.indexOf(" ");
                if (spaceIndex != -1)
                    spaceIndex += term.buffer.normal.cursorX - 3;
            }
            if (spaceIndex != -1) {
                setCursorPosition(spaceIndex + 4, term.buffer.normal.cursorY + 1);
            }
            break;
        case VK_UP:
        case VK_DOWN:
            if (historyCodeList.length === 0) {
                break;
            }
            if (pythonCode.length === 0) {
                pythonCodeX = term.buffer.normal.cursorX + 1;
                pythonCodeY = term.buffer.normal.cursorY + term.buffer.normal.baseY + 1;
            }
            historyCode = "";
            if (e == VK_UP) {
                historyIndex += 1;
                if (historyIndex > (historyCodeList.length + 1)) {
                    historyIndex = historyCodeList.length + 1;
                } else if (historyIndex != (historyCodeList.length + 1)) {
                    historyCode = historyCodeList[historyCodeList.length - historyIndex];
                }
            } else {
                historyIndex -= 1;
                if (historyIndex < 0) {
                    historyIndex = 0;
                } else if (historyIndex != 0) {
                    historyCode = historyCodeList[historyCodeList.length - historyIndex];
                }
            }
            lastCRIndex = pythonCode.lastIndexOf('\r');
            pythonCode = pythonCode.substring(0, lastCRIndex + 1) + historyCode;
            displayCurrentPrompt();
            if (historyCode.length > 0) {
                writeHighlightPythonCode(5, pythonCodeY - term.buffer.normal.baseY, pythonCode)
            }
            break;
        case VK_RETURN:
            if (pythonCode.length > 0) {
                historyIndex = 0;
                let pythonCodeList = pythonCode.split('\r');
                let lastLine = pythonCodeList[pythonCodeList.length - 1];
                if (lastLine.length > 0) {
                    historyCodeList = historyCodeList.concat(lastLine);
                }
                term.writeln('\x1b[0m');
                // We use code.InteractiveInterpreter to take detect incomplete inputs
                pyodide.runPythonAsync(`
                    _PY_code = """
                    ${pythonCode.replaceAll("\\", "\\\\")}
                    """
                    _PY_EVAL.runsource(_PY_code)
                `).then((incomplete: boolean) => {
                    if(incomplete) {
                        pythonCode += "\r";
                        term.write("\r");
                        term.write('... ');
                    } else {
                        pythonCode = '';
                        prompt();
                    }
                }).catch((err: any) => {
                    term.write('\x1b[01;31m' + err.message.replaceAll('\n', '\r\n') + '\x1b[0m');
                    prompt();
                    pythonCode = '';
                });
            } else {
                term.writeln('\x1b[0m');
                prompt();
            }
            break;
        case VK_CANCEL:
            term.write('^C\r\n');
            prompt();
            pythonCode = ""
            break;
        case VK_SUPPR:
        case VK_DELETE:
            let { currentCursorY, lastEditIndex, editIndex } = recalcFromPythonCode();
            if ((e == VK_DELETE && term.buffer.normal.cursorX > 4) || (e == VK_SUPPR && term.buffer.normal.cursorX >= 4) || lastPythonCodeLine.length >= term.cols - 4) {
                // del one char
                if (e == VK_DELETE) {
                    pythonCode = pythonCode.substring(0, lastCRIndex + 1) + lastPythonCodeLine.slice(0, editIndex - 1) + lastPythonCodeLine.slice(editIndex);
                } else {
                    pythonCode = pythonCode.substring(0, lastCRIndex + 1) + lastPythonCodeLine.slice(0, editIndex) + lastPythonCodeLine.slice(editIndex + 1);
                    lastEditIndex += 1;
                }
                hideCursor(term);
                displayCurrentPrompt();
                writeHighlightPythonCode(pythonCodeX, pythonCodeY - term.buffer.normal.baseY, pythonCode).then(() => {
                    if (lastPythonCodeLine.length === term.cols - 4) {
                        setCursorPosition(term.cols, currentCursorY - term.buffer.normal.baseY - 1);
                    } else {
                        setCursorPosition(lastEditIndex + 4, currentCursorY - term.buffer.normal.baseY);
                    }
                    showCursor(term);
                });
            }
            break;
        case VK_CLEAR:
            // reset xterm.js screen
            term.clear();
            break;
        default:
            // debug
            // for (let i = 0; i < e.length; i++) console.log(e.charCodeAt(i));
            // other key pressed
            if (e >= String.fromCharCode(0x20) && e <= String.fromCharCode(0x7E) || e >= '\u00a0') {
                // printable
                if (renderingCode === true) {
                    break;
                }
                renderingCode = true;
                let { currentCursorY, lastEditIndex, editIndex } = recalcFromPythonCode();
                // add one char
                pythonCode = pythonCode.substring(0, lastCRIndex + 1) + lastPythonCodeLine.slice(0, editIndex) + e + lastPythonCodeLine.slice(editIndex);
                term.write('\x1b[?25l');
                writeHighlightPythonCode(pythonCodeX, pythonCodeY - term.buffer.normal.baseY, pythonCode).then(() => {
                    if ((lastEditIndex + 6) > term.cols) {
                        setCursorPosition(0, currentCursorY - term.buffer.normal.baseY + 1);
                    } else {
                        setCursorPosition(lastEditIndex + 6, currentCursorY - term.buffer.normal.baseY);
                    }
                    term.write('\x1b[?25h'); // Show cursor
                    renderingCode = false;
                });
            }
    }
});

// async function scapyInstall() {
//     /*
//      * Install Scapy from ZIP file. This would typically be used if we were doing 1-file builds
//      */
//     let scapyZIP = await fetch(scapyURL);
//     let zipBinary = await scapyZIP.arrayBuffer();
//     await pyodide.unpackArchive(zipBinary, "zip", { extractDir: "/" });
//     const micropip = pyodide.pyimport("micropip");
//     await micropip.install("emfs:/dist/scapy-2.5.0.dev171-py3-none-any.whl")
// }
</script>

<script setup lang="ts">
import { onMounted, onUnmounted } from 'vue';
import { useDisplay } from 'vuetify';

const { smAndDown } = useDisplay();

async function startPyodide() {
    /*
     * Load pyodide and Scapy
     */
    term.write('Loading Python...');
    pyodide = await loadPyodide({
        indexURL: pyodideIndexURL,
    });
    await pyodide.loadPackage("pygments")
    await pyodide.loadPackage("micropip")
    await pyodide.loadPackage("ssl")

    // TODO: move output handlers here... when all Scapy loading issues are fixes

    term.write('\rLoading Scapy... ');
    await pyodide.loadPackage(scapyWheelURL);
    // await scapyInstall();
    await pyodide.runPythonAsync(`
        from scapy.all import *
        conf.color_theme = DefaultTheme()
        import code
        _PY_EVAL = code.InteractiveInterpreter(locals=globals())
    `);

    // Register output stdout / stderr
    pyodide.setStdout({ raw: writeByteOnTerm, isatty: true });
    pyodide.setStderr({ raw: writeByteOnTerm, isatty: true });

    let mini = "False";
    if (smAndDown.value) {
        mini = "True";
    }

    term.write('\r');
    await pyodide.runPythonAsync(`
        import sys
        from pygments import highlight
        from pygments.lexers import PythonLexer
        from pygments.formatters import TerminalTrueColorFormatter
        print(get_fancy_banner(` + mini + `))
    `).then(() => {
        prompt();
        renderingCode = false;
    });
}

// Startup hook
onMounted(async () => {
    // reset existing
    term.clear();
    term.reset();
    historyCodeList = [];
    // start xterm.js and pyodide
    startXterm(term, terminal).then(startPyodide).catch((ex) => {
        disableStdin(term);
        let msg = ex.toString();
        term.write('\rUnexpected failure.           \r\n');
        term.write(msg.replaceAll('\n', '\r\n') + '\r\n');
        try {
            if (msg.includes("WebAssembly") && (navigator.platform.includes("iPhone") || navigator.platform.includes("iPad"))) {
                term.write("On Apple devices, you could be using Lockdown Mode.\r\n");
            }
        } catch { }
    });
});
</script>

<style>
@import '~/xterm/css/xterm.css';
</style>
