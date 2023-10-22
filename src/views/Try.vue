<template>
    <v-row justify="center" class="mt-0 mb-1 px-2 px-sm-0">
        <v-col cols="12" sm="6">
            <TerminalFrame>
                <XTermScapy />
            </TerminalFrame>
        </v-col>
        <v-col cols="12" sm="3">
            <v-card variant="tonal">
                <v-card-title>
                    Try Scapy in your browser !
                </v-card-title>
                <v-card-text>
                    <p>
                        You can <span class="text-primary">try Scapy</span> in the Terminal on the left.
                    </p>
                    <p class="mt-3">
                        Please note that the experience is very limited, most notably:
                    </p>
                    <ul class="ml-5">
                        <li>All <span class="text-red">I/O functions will not work</span> (send, sr, sniff, ...) !</li>
                        <li>Anything that uses an external package (matplotlib, pyx, ...) is unsupported.</li>
                    </ul>
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>
</template>

<script lang="ts" setup>
import TerminalFrame from '@/components/TerminalFrame.vue';
import XTermScapy from '@/components/XTermScapy.vue';
</script>