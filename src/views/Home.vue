<template>
  <div>
    <!-- The animated Scapy logo box -->
    <v-row justify="center">
      <v-col cols="11" class="mb-3">
        <v-row align="center" justify="center" aria-hidden="true">
          <v-col cols="auto" class="pa-0 pr-2">
            <ScapyS />
          </v-col>
          <v-col cols="6" lg="4" class="px-0">
            <v-fade-transition>
              <div v-show="animationOk" color="transparent" class="scapy-main-box fill-height px-0 text-blue-lighten-2">
                <template v-if="!smAndDown">
                  | <br />
                </template>
                | Welcome to Scapy<br />
                | Version {{ version }}<br />
                | <br />
                | <span class='text-secondary'><a href="https://github.com/secdev/scapy"><span
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
              </div>
            </v-fade-transition>
          </v-col>
        </v-row>
        <v-row>
          <!-- What is Scapy -->
          <v-col cols="12" lg="7" class="d-flex">
            <v-card variant="tonal">
              <v-card-title>
                <h4>What is Scapy?</h4>
              </v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="12" sm="4">
                    <p class="pb-2 text-body-1">
                      <span class="font-weight-bold">Manipulate packets</span>
                    </p>
                    <p>
                      Scapy is a powerful <span class="text-primary">interactive packet manipulation library</span>
                      written in <span>Python</span>.
                      Scapy is able to forge or decode packets of a wide number of protocols, send them on the wire,
                      capture
                      them, match requests and replies, and much more.
                    </p>
                  </v-col>
                  <v-col cols="12" sm="4">
                    <p class="pb-2 text-body-1">
                      <span class="font-weight-bold">A REPL and a Library</span>
                    </p>
                    <p>
                      Scapy can be used <span class="text-primary">as a REPL</span> or <span class="text-primary">as
                        a library</span>. It provides all the tools and documentation to quickly add custom network
                      layers.
                    </p>
                  </v-col>
                  <v-col cols="12" sm="4">
                    <p class="pb-2 text-body-1">
                      <span class="font-weight-bold">Cross-platform</span>
                    </p>
                    <p>
                      Scapy runs natively on Linux, macOS, most Unixes, and on Windows with Npcap.
                      It is published under <a href="https://www.gnu.org/licenses/gpl-2.0"
                        class="text-decoration-none text-primary">GPLv2</a>.<br />
                      Starting from version 2.5.0+, it supports <span class="text-primary">Python
                        3.7+</span> (and PyPy).<br />
                    </p>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <!-- Shell demo -->
          <v-col cols="12" lg="5">
            <TerminalFrame>
              <XTerm :static="DEMO_CODE" class="scapy-term" />
            </TerminalFrame>
          </v-col>
          <!-- Documentation -->
          <v-col cols="12" lg="8">
            <v-card variant="tonal">
              <v-card-title>
                <h4>Documentation</h4>
              </v-card-title>
              <v-card-text class="text-body-2 align-content-center">
                <p>
                  The official Scapy documentation can be found online on readthedocs:
                </p>
                <v-row justify="center" class="py-3">
                  <v-col cols="auto">
                    <v-btn href="https://scapy.readthedocs.io/" color="secondary">
                      Documentation
                      <v-icon class="ml-1" :icon="mdiOpenInNew"></v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
                <p>
                  But there are other good introductions out there, most notably:
                <ul class="ml-5">
                  <li><a class="text-secondary"
                      href="https://guedou.github.io/talks/2022_GreHack/Scapy in 0x30 minutes.slides.html">Scapy
                      in 0x30 minutes</a> (<a class="text-secondary"
                      href="https://github.com/guedou/guedou.github.io/blob/master/talks/2022_GreHack/Scapy%20in%200x30%20minutes.ipynb">notebook</a>)
                    by guedou</li>
                  <li><a class="text-secondary"
                      href="https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb">Scapy
                      in 15 minutes (or longer)</a>, made guedou and p-l-</li>
                  <li><a class="text-secondary" href="https://guedou.github.io/talks/2021_sharkfest/slides.pdf">Scapy
                      Turned 18. Boy They Grow Up Fast, Don’t They - SharkFest’21 Keynote</a> (<a class="text-secondary"
                      href="https://www.youtube.com/watch?v=krZ3fOCTlfs">video</a>), by guedou</li>
                  <li>ThePacketGeek's <a class="text-secondary"
                      href="https://thepacketgeek.com/scapy/building-network-tools/">"Building Network Tools with Scapy
                      tutorial"</a></li>
                  <li><a class="text-secondary" href="https://www.oreilly.com/catalog/9780596009632/">Security Power
                      Tools</a> where Philippe Biondi wrote a complete chapter about Scapy</li>
                  <li>A bunch (<a class="text-secondary"
                      href="https://boutique.ed-diamond.com/home/863-misc-hs-11.html">MISC HS 11</a>, <a
                      class="text-secondary"
                      href="https://boutique.ed-diamond.com/numeros-deja-parus/354-misc52.html">MISC
                      52</a>, <a class="text-secondary"
                      href="https://boutique.ed-diamond.com/les-hors-series/1245-gnulinux-magazine-hs-90.html">GNU
                      HS90</a>)
                    of articles in French Security Magazines</li>
                </ul>
                </p>
                <p class="mt-3">
                  This website also hosts several conferences related to Scapy, some of which can provide details
                  regarding
                  certain parts of Scapy:
                <ul class="ml-5">
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/troopers2022/main.slides.html'">Automotive
                      Network
                      Scans with Scapy - Troopers 2022
                      slides</a></li>
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/troopers2019/index.html'">Automotive Penetration
                      Testing with Scapy - Troopers 2019
                      slides</a></li>
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/scapy_pacsec05.pdf'">Scapy’s PacSec/core05
                      slides</a> (<a class="text-secondary"
                      :href="BASE_URL + 'talks/scapy_pacsec05.handout.pdf'">printable
                      version</a>)</li>
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/scapy_hack.lu.pdf'">Scapy’s Hack.lu 2005
                      slides</a>
                  </li>
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/scapy_Aachen.pdf'">Scapy’s Summerschool Applied
                      IT
                      Security 2005 slides</a></li>
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/scapy_T2.pdf'">Scapy’s T2’2005 slides</a></li>
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/scapy_csw05.pdf'">Scapy’s CanSecWest/core05
                      slides</a></li>
                  <li><a class="text-secondary" :href="BASE_URL + 'talks/scapy_lsm2003.pdf'">Scapy’s LSM 2003 slides</a>
                  </li>
                </ul>
                </p>
                <p class="mt-3">
                  Finally, note that we have an <a class="text-secondary"
                    href="https://github.com/secdev/awesome-scapy">awesome-scapy</a> page, where we try to reference cool
                  projects that make use of Scapy.
                </p>
              </v-card-text>
            </v-card>
          </v-col>
          <!-- Maintainers -->
          <v-col cols="12" lg="4" class="d-flex flex-column">
            <v-card variant="tonal" class="flex-grow-1 flex-shrink-1">
              <v-card-title>
                <h4>Maintainers</h4>
              </v-card-title>
              <v-card-text class="text-body-2">
                <v-row>
                  <v-col cols="6" sm="4" lg="6">
                    <SponsorCard user="gpotter2" userid="10530980" />
                  </v-col>
                  <v-col cols="6" sm="4" lg="6">
                    <SponsorCard user="p-l-" userid="5064814" />
                  </v-col>
                  <v-col cols="6" sm="4" lg="6">
                    <SponsorCard user="guedou" userid="11683796" />
                  </v-col>
                  <v-col cols="6" sm="4" lg="6">
                    <SponsorCard user="polybassa" userid="1676055" />
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <!-- Downloads -->
          <v-col cols="12">
            <div ref="downloads_section">
              <v-card variant="tonal">
                <v-card-title>
                  <h4>Downloads & Installation</h4>
                </v-card-title>
                <v-card-text class="text-body-2">
                  <p>
                    There are several ways of installing Scapy, depending on your plateform.
                  </p>
                  <p class="pb-3">
                    Please also have a look at the
                    full documentation, which contains
                    <a href="https://scapy.readthedocs.io/en/latest/installation.html" class="text-primary">more
                      installation
                      instructions.
                    </a>
                  </p>
                  <v-card color="transparent">
                    <v-tabs show-arrows v-model="dllTab" bg-color="primary" density="compact" slider-color="#314C46">
                      <v-tab value="pypi">PyPI</v-tab>
                      <v-tab value="windows">Windows</v-tab>
                      <v-tab value="github">Github</v-tab>
                      <v-tab value="conda">Conda</v-tab>
                      <v-tab value="debian">Debian/Ubuntu</v-tab>
                      <v-tab value="other">More</v-tab>
                    </v-tabs>
                    <v-card-text>
                      <v-window v-model="dllTab">
                        <v-window-item value="pypi">
                          <code class="bash"><span class="text-secondary">pip install scapy</span></code>
                        </v-window-item>
                        <v-window-item value="github">
                          <code
                            class="bash"><span class="text-secondary">pip install https://github.com/secdev/scapy/archive/refs/heads/master.zip</span></code>
                        </v-window-item>
                        <v-window-item value="conda">
                          <code class="bash"><span class="text-secondary">conda install -c conda-forge scapy</span></code>
                        </v-window-item>
                        <v-window-item value="debian">
                          <code class="bash"><span class="text-secondary">sudo apt install python3-scapy</span></code>
                        </v-window-item>
                        <v-window-item value="windows">
                          <p class="pb-2">
                            You will need to install <a class="text-secondary"
                              href="https://npcap.com/#download">Npcap</a>
                            (included if you have Wireshark), then use another installation method (PyPI, Github, etc.)
                          </p>
                          <v-btn href="https://npcap.com/#download" color="secondary">
                            Download Npcap
                            <v-icon class="ml-1" :icon="mdiOpenInNew"></v-icon>
                          </v-btn>
                        </v-window-item>
                        <v-window-item value="other">
                          <p class="pb-2">
                            More platform-specific instructions (MacOS, BSD...) are available in the full documentation:
                          </p>
                          <v-btn
                            href="https://scapy.readthedocs.io/en/latest/installation.html#platform-specific-instructions"
                            color="secondary">
                            Other instructions
                            <v-icon class="ml-1" :icon="mdiOpenInNew"></v-icon>
                          </v-btn>
                        </v-window-item>
                      </v-window>
                    </v-card-text>
                  </v-card>
                </v-card-text>
              </v-card>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts" setup>
import ScapyS from '@/components/ScapyS.vue'
import SponsorCard from '@/components/SponsorCard.vue'
import TerminalFrame from '@/components/TerminalFrame.vue'
import XTerm from '@/components/XTerm.vue'

import { useDisplay } from 'vuetify';
import { inject, computed, onMounted, ref, watchEffect } from 'vue';
import type { Ref } from 'vue'

import { mdiOpenInNew } from '@mdi/js';

const version = '2.5.0';

const animationOk = ref(false);
const downloads_section = inject<Ref<HTMLDivElement | null>>('downloads_section');

const { smAndDown, lg } = useDisplay();
/* Wait 1s (animation time), if big screen, then display Home */
onMounted(() => {
  if (smAndDown.value) {
    animationOk.value = true;
  } else {
    setTimeout(() => {
      animationOk.value = true;
    }, 1000);
  }
});

/* Size of quote text and XTerm.js */
const fontSize = ref('1em');
const maxTermHeight = ref('300px');
watchEffect(() => {
  /* Select font size based on display size */
  if (smAndDown.value) {
    fontSize.value = '0.8em';
  } else {
    fontSize.value = '1em';
  }
  if (lg.value) {
    maxTermHeight.value = '300px';
  } else {
    maxTermHeight.value = '300px';
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
Welcome to Scapy (` + version + `)
\x1b[34m\x1b[1m>>>\x1b[0m pkt = Ether() / IP(dst=\x1b[38:5:208m"github.com"\x1b[0m) / ICMP()
\x1b[34m\x1b[1m>>>\x1b[0m resp = srp1(pkt, iface=\x1b[38:5:208m"eth0"\x1b[0m, timeout=\u001b[38;5;34m1\x1b[0m)
Begin emission:
Finished sending 1 packets.
.*
Received 2 packets, got 1 answers, remaining 0 packets
\x1b[34m\x1b[1m>>>\x1b[0m resp[IP].show()
\x1b[0m###[\x1b[0m \x1b[31m\x1b[1mICMP\x1b[0m \x1b[0m]###\x1b[0m
  \x1b[34mtype\x1b[0m      \x1b[0m=\x1b[0m \x1b[35mecho-reply\x1b[0m
  \x1b[34mcode\x1b[0m      \x1b[0m=\x1b[0m \x1b[35m0\x1b[0m
  \x1b[34mchksum\x1b[0m    \x1b[0m=\x1b[0m \x1b[35m0xffff\x1b[0m
  \x1b[34mid\x1b[0m        \x1b[0m=\x1b[0m \x1b[35m0x0\x1b[0m
  \x1b[34mseq\x1b[0m       \x1b[0m=\x1b[0m \x1b[35m0x0\x1b[0m
  \x1b[34munused\x1b[0m    \x1b[0m=\x1b[0m \x1b[35mb''\x1b[0m
`;

/* Download tabs */
const dllTab = ref("pypi");

/* Export base URL */
const BASE_URL = import.meta.env.BASE_URL;
</script>

<style scoped>
/* Main Title box */
.scapy-main-box {
  /* Monospace font */
  font-family: Courier New, Courier, Lucida Sans Typewriter, Lucida Typewriter, monospace;
  font-size: v-bind(fontSize);
  white-space: pre;
}

/* Side terminal */
.scapy-term {
  max-height: v-bind(maxTermHeight);
}

/* Don't display different color for visited links */
a,
a:visited {
  color: inherit;
}

/* Bash line */
code.bash:before {
  content: '$ ';
}

/* Thinner h4 titles */
h4 {
  font-weight: 500;
  padding: 2px 0px 2px 0px;
}
</style>
