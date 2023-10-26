<template>
    <v-row justify="center" class="mt-0 mb-1 px-2 px-lg-0">
        <v-col cols="12" lg="6" class="pb-0">
            <TerminalFrame>
                <XTermScapy />
            </TerminalFrame>
        </v-col>
        <v-col cols="12" lg="4">
            <v-card variant="tonal">
                <v-card-title>
                    Try Scapy in your browser !
                </v-card-title>
                <v-card-text>
                    <p>
                        You can <span class="text-primary">try Scapy</span> in the nearby Terminal. It's running locally
                        thanks to <a href="https://pyodide.org/" class="text-secondary">Pyodide</a> and <a
                            href="https://emscripten.org/" class="text-secondary">Emscripten</a>.
                    </p>
                    <p class="mt-3">
                        Please note that the experience is very limited, most notably:
                    </p>
                    <ul class="ml-5">
                        <li><span class="text-red font-weight-bold">I/O functions will NOT work !</span> (send, sr, sniff, etc.)</li>
                        <li>Anything that uses an external package (matplotlib, pyx, ...) is unsupported.</li>
                    </ul>
                    <p class="mt-3">
                        Try to upload a pcap file and use <span class="text-primary">rdpcap("file.pcap")</span> !
                    </p>
                </v-card-text>
            </v-card>
            <!-- Drag and drop -->
            <input type="file" multiple style="display: none" @change="onChange" ref="fileSelector"
                accept=".pcap.gz, .pcapng, .pcap" />
            <v-card variant="outlined" :class="'mt-4 py-5 ' + (overlay ? 'overlay' : '')"
                @dragenter="dragenter" @dragover="dragover" @dragleave="dragleave" @drop="drop" @click="trigger">
                <v-card-text class="text-center">
                    <p class="text-h5">
                        <span class="text-primary">Drop a pcap file here</span>
                    </p>
                    (everything is running locally in your browser)
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
</template>

<script lang="ts" setup>
import { ref, Ref } from 'vue';

import TerminalFrame from '@/components/TerminalFrame.vue';
import XTermScapy from '@/components/XTermScapy.vue';
import { mountFile } from '@/components/XTermScapy.vue';

// function to process files

function processFiles(files: FileList) {
    /*
     * Mount all files in emscripten
     */
    for (let i = 0; i < files.length; i++) {
        let file = files[i];
        mountFile(file);
    }
}

// drag & drop utils

const dragCounter = ref(0);
const overlay = ref(false);
const fileSelector: Ref<HTMLInputElement | null> = ref(null);

function trigger() {
    fileSelector?.value?.click();
}

function dragover(event: Event) {
    event.preventDefault();
}

function dragenter(event: Event) {
    event.preventDefault();
    dragCounter.value++;
    overlay.value = true;
}

function dragleave(event: Event) {
    event.preventDefault();
    dragCounter.value--;
    if (dragCounter.value == 0) {
        overlay.value = false;
    }
}

function onChange() {
    const files = fileSelector?.value?.files;
    if (files)
        processFiles(files);
}

function drop(event: DragEvent) {
    event.preventDefault();
    dragCounter.value = 0;
    overlay.value = false;
    if (event.dataTransfer)
        processFiles(event.dataTransfer.files);
}
</script>

<style scoped>
.overlay {
    background: #7a7a79;
}
</style>