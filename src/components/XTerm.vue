<template>
    <div id="terminal" ref="terminal" style="height: 100%;"></div>
</template>

<script setup lang="ts">
import { onMounted, ref, Ref } from 'vue';
import { Terminal } from 'xterm';
import { useDisplay } from 'vuetify';

const props = defineProps({
    static: String,
});

const terminal: Ref<HTMLElement | null> = ref(null);
const term = new Terminal();

if (props.static) {
    disableStdin(term);
    // now print static text
    term.write(props.static.replaceAll("\n", "\r\n"));
}

onMounted(async () => {
    await startXterm(term, terminal);
});
</script>

<script lang="ts">
import { FitAddon } from 'xterm-addon-fit';

export async function startXterm(term: Terminal, terminal: Ref<HTMLElement | null>) {
    /*
     * Load xterm.js
     */
    // Load fit plugin
    const fitAddon = new FitAddon();
    term.loadAddon(fitAddon);
    // Configure font size
    const { sm, xs } = useDisplay();
    if (xs.value) {
        term.options.fontSize = 10;
    } else if (sm.value) {
        term.options.fontSize = 13;
    } else {
        term.options.fontSize = 15;
    }
    // Display
    if (!terminal.value) {
        console.log("Could not load Xterm.js terminal !");
        return;
    }
    term.open(terminal.value);
    fitAddon.fit();
}

export function hideCursor(term: Terminal) {
    term.write('\x1b[?25l');
}

export function showCursor(term: Terminal) {
    term.write('\x1b[?25h');
}

export function disableStdin(term: Terminal) {
    // Fully disable input
    term.options.disableStdin = true;
    term.options.cursorInactiveStyle = "none";
    hideCursor(term);
}
</script>

<style>
@import '~/xterm/css/xterm.css';
</style>