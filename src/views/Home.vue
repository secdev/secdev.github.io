<template>
  <div>
    <!-- The animated Scapy logo box -->
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="auto" class="pl-0">
          <ScapyS />
        </v-col>
        <v-col cols="6" class="px-0">
          <v-fade-transition>
            <v-card v-show="animationOk">
              <v-card-text class="scapy-main-box fill-height px-0 text-blue-lighten-2">
                <template v-if="!smAndDown">
                  | <br />
                </template>
                | Welcome to Scapy<br />
                | Version {{ version }}<br />
                | <br />
                | <span class='text-blue-lighten-4'><a href="https://github.com/secdev/scapy"><span
                      class="hidden-xs">https://github.com/</span>secdev/scapy</a>
                </span><br />
                | <br />
                | Have fun!<br />
                <template v-if="!smAndDown">
                  | <br />
                  | {{ quote[0] }}<br />
                  | {{ quote[1] }}<br />
                  | {{ quote[2] }}<br />
                  | <br />
                </template>
              </v-card-text>
            </v-card>
          </v-fade-transition>
        </v-col>
      </v-row>
      <v-row>
        <!-- What is Scapy -->
        <v-col cols="12" lg="7" class="d-flex">
          <v-card variant="tonal">
            <v-card-title>What is Scapy?</v-card-title>
            <v-card-text>
              <v-row>
                <v-col cols="12" sm="4">
                  <p class="pb-2 text-body-1">
                    <span class="font-weight-bold">Manipulate packets</span>
                  </p>
                  <p>
                    Scapy is powerful <span class="text-lime-lighten-2">interactive packet manipulation libary</span>
                    written in <span>Python</span>.
                    Scapy is able to forge or decode packets of a wide number of protocols, send them on the wire, capture
                    them, match requests and replies, and much more.
                  </p>
                </v-col>
                <v-col cols="12" sm="4">
                  <p class="pb-2 text-body-1">
                    <span class="font-weight-bold">A REPL and a Library</span>
                  </p>
                  <p>
                    Scapy can be used <span class="text-lime-lighten-2">as a REPL</span>, to quickly craft-and-send,
                    sniff.. custom packets over the network, or <span class="text-lime-lighten-2">as
                      a library</span>. It provides all the tools and documentation to quickly add custom network layers.
                  </p>
                </v-col>
                <v-col cols="12" sm="4">
                  <p class="pb-2 text-body-1">
                    <span class="font-weight-bold">Cross-platform</span>
                  </p>
                  <p>
                    Scapy runs natively on Linux, Windows, OSX and on most Unixes with libpcap.<br />
                    Starting from version 2.5.0+, it has has support for <span class="text-lime-lighten-2">Python
                      3.7+</span> (and PyPy).
                  </p>
                </v-col>
              </v-row>
            </v-card-text>
          </v-card>
        </v-col>
        <!-- Shell demo -->
        <v-col cols="12" lg="5" class="d-flex flex-column">
          <v-card variant="tonal" class="full-height flex-grow-1 flex-shrink-1">
            <v-card-title>Shell demo</v-card-title>
            <v-card-text class="text-body-2">
              <pre style="white-space: pre-wrap;" v-html="DEMO_CODE"></pre>
            </v-card-text>
          </v-card>
        </v-col>
        <!-- Documentation -->
        <v-col cols="12">
          <v-card variant="tonal">
            <v-card-title>Documentation</v-card-title>
            <v-card-text class="text-body-2">
              The followings are good heads
            </v-card-text>
          </v-card>
        </v-col>
        <!-- Downloads -->
        <v-col cols="12">
          <div ref="downloads_section">
            <v-card variant="tonal">
              <v-card-title>Downloads</v-card-title>
              <v-card-text class="text-body-2">
                yolo
              </v-card-text>
            </v-card>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts" setup>
import ScapyS from '@/components/ScapyS.vue'

import { useDisplay } from 'vuetify';
import { inject, computed, onMounted, ref } from 'vue';
import type { Ref } from 'vue'

const version = '2.5.0';

const animationOk = ref(false);
const downloads_section = inject<Ref<HTMLDivElement | null>>('downloads_section');


/* Wait 1s (animation time), if big screen, then display Home */
const { smAndDown } = useDisplay();
onMounted(() => {
  if (smAndDown.value) {
    animationOk.value = true;
  } else {
    setTimeout(() => {
      animationOk.value = true;
    }, 1000);
  }
});

/* Quotes database: web-oriented, unlike the ones in actual Scapy */
const AVAILABLE_QUOTES = [
  ["Craft packets like it is your last day on earth.", "Lao-Tze"],
  ["Craft packets like I craft my beer.", "Jean De Clerck"],
  ["Craft packets before they craft you.", "Socrate"],
  ["Craft me if you can.", "IPv6 layer"],
  ["To craft a packet, you have to be a packet, and learn how to swim in the wires and in the waves.", "Jean-Claude Van Damme"],
  ["We are in France, we say Skappee. OK? Merci.", "Sebastien Chabal"],
  ["Wanna support scapy? Star us on GitHub!", "Satoshi Nakamoto"],
  ["What is dead may never die!", "Python 2"],
];
const quote = computed(() => {
  let selected = AVAILABLE_QUOTES[Math.floor(AVAILABLE_QUOTES.length * Math.random())];
  return [
    ...(selected[0].match(/.{1,50}/g) || []), /* Quote, max size of line: 20 */
    ' '.repeat(22) + "-- " + selected[1], /* Author */
  ]
});

/* Demo code */
const DEMO_CODE = `\
$ sudo scapy -H
Welcome to Scapy (2.5.0)
<span class="text-blue">&gt;&gt;&gt;</span> pkt = Ether()/IP(dst=<span class="text-orange">"github.com"</span>)/ICMP()
<span class="text-blue">&gt;&gt;&gt;</span> resp = srp1(pkt, iface=<span class="text-orange">"eth0"</span>, timeout=1)
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
<span class="text-blue">&gt;&gt;&gt;</span> resp[ICMP]
&lt;<span class="text-red">ICMP</span> <span class="text-blue">type</span>=<span class="text-purple">echo-reply</span> <span class="text-blue">code</span>=<span class="text-purple">0</span> <span class="text-blue">chksum</span>=<span class="text-purple">0xffff</span> <span class="text-blue">id</span>=<span class="text-purple">0x0</span> <span class="text-blue">seq</span>=<span class="text-purple">0x0</span> |&gt;
`;
</script>

<style scoped>
.scapy-main-box {
  /* Monospace font */
  font-family: Courier New, Courier, Lucida Sans Typewriter, Lucida Typewriter, monospace;
  white-space: pre;
}

/* Don't display different color for visited links */
a,
a:visited {
  color: inherit;
}
</style>