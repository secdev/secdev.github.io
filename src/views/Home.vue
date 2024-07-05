<template>
  <div>
    <!-- The animated Scapy logo box -->
    <v-row justify="center">
      <v-col cols="11" class="mb-4">
        <v-row align="center" justify="center" aria-hidden="true">
          <v-col cols="auto" class="pt-3 pb-0 pl-0 pr-2">
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
            <TerminalFrame style="position: relative;">
              <XTerm :static="DEMO_CODE" class="scapy-term" />
              <div style="position: absolute; right: 5px; bottom: 5px;">
                <v-tooltip text="Try Scapy" location="start">
                  <template v-slot:activator="{ props }">
                    <v-btn v-bind="props" class="px-0" min-width="36px" color="yellow" @click="setTryScapy(true)">
                      <span class="font-weight-bold">>_</span>
                    </v-btn>
                  </template>
                </v-tooltip>
              </div>
            </TerminalFrame>
          </v-col>
          <!-- Documentation -->
          <v-col cols="12" lg="8">
            <v-card variant="tonal">
              <v-card-title>
                <h4>Documentation</h4>
              </v-card-title>
              <v-card-text class="text-body-2 align-content-center">
                <!-- Emphasis on the official doc -->
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
                  The official documentation is <span class="text-primary font-weight-bold">probably the best way of
                    learning Scapy</span>, as it's the only up-to-date official resource.
                  That being said, there are many other good resources, some of which are listed below.
                </p>
                <br />
                <!-- Resources -->
                <span class="text-h6">Good introductions to Scapy</span>
                <v-table class="mb-2" density="compact">
                  <thead>
                    <tr>
                      <th class="text-left">Title</th>
                      <th class="text-left">Links</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, i) in RESOURCES" :key="i">
                      <td><span class="text-primary">{{ item.title }}</span> by {{ item.author }}</td>
                      <td>
                        <div class="overflow-hidden text-no-wrap">
                          <v-tooltip :text="link.tooltip" v-for="(link, j) in item.links" :key="j">
                            <template v-slot:activator="{ props }">
                              <v-btn v-bind="props" :icon="link.icon" variant="plain" :href="link.link" color="secondary"
                                :size="smAndDown ? 'x-small' : 'small'"></v-btn>
                            </template>
                          </v-tooltip>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </v-table>
                <!-- Conferences -->
                <span class="text-h6">Conferences</span>
                <v-table density="compact">
                  <thead>
                    <tr>
                      <th class="text-left" v-show="smAndUp">Title</th> <!-- Not shown on mobile -->
                      <th class="text-left">Venue</th>
                      <th class="text-left">Links</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, i) in CONFERENCES" :key="i">
                      <td v-show="smAndUp"><span class="text-primary">{{ item.title }}</span></td>
                      <td>
                        {{ item.venue }}
                      </td>
                      <td>
                        <div class="overflow-hidden text-no-wrap">
                          <v-tooltip :text="link.tooltip" v-for="(link, j) in item.links" :key="j">
                            <template v-slot:activator="{ props }">
                              <v-btn v-bind="props" :icon="link.icon" variant="plain" :href="link.link" color="secondary"
                                :size="smAndDown ? 'x-small' : 'small'"></v-btn>
                            </template>
                          </v-tooltip>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </v-table>
                <p class="mt-3">
                  Finally, note that we have an <a class="text-secondary font-weight-bold"
                    href="https://github.com/secdev/awesome-scapy">awesome-scapy</a> page, where we try to reference cool
                  projects that make use of Scapy.
                </p>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" lg="4" class="d-flex flex-column">
            <!-- Maintainers -->
            <v-container fluid class="pa-0">
              <v-card variant="tonal">
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
            </v-container>
            <!-- Downloads -->
            <v-container fluid class="px-0 pb-0 pt-6 d-flex flex-column flex-grow-1">
              <div ref="downloads_section" class="flex-grow-1">
                <v-card variant="tonal" class="fill-height">
                  <v-card-title>
                    <h4>Downloads & Installation</h4>
                  </v-card-title>
                  <v-card-text class="text-body-2">
                    <p>
                      There are several ways of installing Scapy, depending on your plateform.
                    </p>
                    <p>
                      Please also have a look at the
                      full documentation, which contains
                      <a href="https://scapy.readthedocs.io/en/latest/installation.html" class="text-primary">
                        more installation instructions.
                      </a>
                    </p>
                    <v-row class="py-2 ma-0" justify="center">
                      <!-- OS picker -->
                      <v-col cols="12" class="py-0">
                        <p class="text-center text-h6 pa-0">
                          Choose your OS
                        </p>
                      </v-col>
                      <v-col cols="auto" class="pb-1">
                        <v-btn-toggle v-model="dllOS" mandatory>
                          <v-btn v-for="os in OS" :value="os.name" :key="os.name" icon
                            :size="smAndDown ? 'small' : 'default'">
                            <v-icon v-if="os.logo"><v-img :src="os.logo" /></v-icon>
                            <span v-else>{{ os.text }}</span>
                          </v-btn>
                        </v-btn-toggle>
                      </v-col>
                    </v-row>
                    <v-row class="pb-2 ma-0" justify="center">
                      <!-- Env picker -->
                      <v-col cols="12" class="py-0">
                        <p class="text-center text-h6">
                          Choose an install method
                        </p>
                      </v-col>
                      <v-col cols="auto">
                        <v-btn-toggle v-model="dllMethod" mandatory>
                          <v-btn v-for="method in getMethods()" :value="method.name" :key="method.name" icon
                            :size="smAndDown ? 'small' : 'default'">
                            <v-icon><v-img :src="method.logo" /></v-icon>
                          </v-btn>
                        </v-btn-toggle>
                      </v-col>
                    </v-row>
                    <v-card>
                      <v-card-text>
                        <!-- OS specific instructions -->
                        <p class="pb-2" v-show="dllOS == 'windows'">
                          You will need to install <a class="text-secondary" href="https://npcap.com/">Npcap</a>
                          (included if you have Wireshark).
                        </p>
                        <p class="pb-2" v-show="dllOS == 'other'">
                          More platform-specific instructions (MacOS, BSD...) are available in the full documentation:
                        </p>
                        <p class="pb-2" v-show="dllOS == 'linux'">
                          Some features require to have <span class="text-primary">libpcap</span> installed (by default on
                          most distributions). For more
                          information, see the <a
                            href="https://scapy.readthedocs.io/en/latest/installation.html#platform-specific-instructions"
                            class="text-secondary">full
                            documentation</a>.
                        </p>
                        <p class="text-center" v-show="dllOS == 'windows'">
                          <v-btn href="https://npcap.com/#download" color="secondary">
                            Download Npcap
                            <v-icon class="ml-1" :icon="mdiOpenInNew"></v-icon>
                          </v-btn>
                        </p>
                        <p class="text-center" v-show="dllOS == 'other'">
                          <v-btn
                            href="https://scapy.readthedocs.io/en/latest/installation.html#platform-specific-instructions"
                            color="secondary">
                            More instructions
                            <v-icon class="ml-1" :icon="mdiOpenInNew"></v-icon>
                          </v-btn>
                        </p>

                      </v-card-text>
                    </v-card>
                    <div class="text-center pa-1 font-weight-bold">
                      AND
                    </div>
                    <v-card>
                      <v-card-text>
                        <!-- Methods -->
                        <code class="bash"><span class="text-secondary">{{ INSTRUCTIONS[dllMethod] }}</span></code>
                      </v-card-text>
                    </v-card>
                  </v-card-text>
                </v-card>
              </div>
            </v-container>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
    <!-- Try Scapy -->
    <v-dialog v-if="showTryScapy" :model-value="showTryScapy" fullscreen>
      <v-toolbar dark color="primary" density="compact">
        <v-btn icon dark @click="setTryScapy(false)">
          <v-icon :icon="mdiClose"></v-icon>
        </v-btn>
        Scapy DEMO
      </v-toolbar>
      <v-card class="d-block">
        <Try></Try>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts" setup>
import ScapyS from '@/components/ScapyS.vue'
import SponsorCard from '@/components/SponsorCard.vue'
import TerminalFrame from '@/components/TerminalFrame.vue'
import XTerm from '@/components/XTerm.vue'
import Try from '@/views/Try.vue'

import { useDisplay } from 'vuetify';
import { inject, computed, onMounted, ref, watchEffect } from 'vue';
import { useRoute, useRouter } from 'vue-router';

import type { Ref } from 'vue';

import {
  mdiBook,
  mdiClose,
  mdiOpenInNew,
  mdiPresentation,
  mdiPresentationPlay,
  mdiNotebook,
  mdiWeb,
} from '@mdi/js';

const version = '2.5.0';

const animationOk = ref(false);
const downloads_section = inject<Ref<HTMLDivElement | null>>('downloads_section');

/* Modal control */
const route = useRoute();
const showTryScapy = computed(() => {
  return Boolean(route.query.try);
});
const router = useRouter();
function setTryScapy(set: Boolean) {
  if (set) {
    router.push({ query: { try: 1 } })
  } else {
    router.push({});
  }
}

const { smAndDown, smAndUp, lg } = useDisplay();
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
  \x1b[34munused\x1b[0m    \x1b[0m=\x1b[0m \x1b[35mb''\x1b[0m`;

/* Export base URL */
const BASE_URL = import.meta.env.BASE_URL;

/* Resources */
const RESOURCES = [
  {
    title: "Scapy in 0x30 minutes",
    author: "guedou",
    links: [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: "https://guedou.github.io/talks/2022_GreHack/Scapy in 0x30 minutes.slides.html",
      },
      {
        tooltip: "Notebook",
        icon: mdiNotebook,
        link: "https://github.com/guedou/guedou.github.io/blob/master/talks/2022_GreHack/Scapy%20in%200x30%20minutes.ipynb"
      }
    ]
  },
  {
    title: "Scapy in 15 minutes (or longer)",
    author: "guedou and p-l-",
    links: [
      {
        tooltip: "Notebook",
        icon: mdiNotebook,
        link: "https://github.com/secdev/scapy/blob/master/doc/notebooks/Scapy%20in%2015%20minutes.ipynb"
      }
    ]
  },
  {
    title: "Scapy Turned 18. Boy They Grow Up Fast, Don’t They - SharkFest’21 Keynote",
    author: "guedou",
    links: [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: "https://guedou.github.io/talks/2021_sharkfest/slides.pdf"
      },
      {
        tooltip: "Video",
        icon: mdiPresentationPlay,
        link: "https://www.youtube.com/watch?v=krZ3fOCTlfs"
      },
    ]
  },
  {
    title: "ThePacketGeek.com's Building Network Tools with Scapy tutorial",
    author: "thePacketGeek",
    links: [
      {
        tooltip: "Website",
        icon: mdiWeb,
        link: "https://thepacketgeek.com/scapy/building-network-tools/"
      }
    ]
  },
  {
    title: "Security Power Tools",
    author: "Philippe Biondi",
    links: [
      {
        tooltip: "Book",
        icon: mdiBook,
        link: "https://www.oreilly.com/catalog/9780596009632/",
      }
    ]
  },
  // Commented out. Unobtainable at this point
  // {
  //   title: "Various articles in French Security Magazines",
  //   author: "Philippe Biondi",
  //   links: [
  //     {
  //       tooltip: "MISC HS 11",
  //       icon: mdiBook,
  //       link: "https://boutique.ed-diamond.com/home/863-misc-hs-11.html",
  //     },
  //     {
  //       tooltip: "MISC 52",
  //       icon: mdiBook,
  //       link: "https://boutique.ed-diamond.com/numeros-deja-parus/354-misc52.html",
  //     },
  //     {
  //       tooltip: "GNU HS90",
  //       icon: mdiBook,
  //       link: "https://boutique.ed-diamond.com/les-hors-series/1245-gnudebian-magazine-hs-90.html",
  //     }
  //   ]
  // }
]

/* Conferences */
const CONFERENCES = [
  {
    "title": "ScapyCon Automotive",
    "venue": "ScapyCon 2024",
    "links": [
      {
        tooltip: "Website",
        icon: mdiWeb,
        link: "https://scapycon.com"
      }
    ]
  },
  {
    "title": "Automotive Network Scans with Scapy",
    "venue": "Troopers 2022",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/troopers2022/main.slides.html",
      }
    ]
  },
  {
    "title": "Automotive Penetration Testing with Scapy",
    "venue": "Troopers 2019",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/scapy_pacsec05.pdf",
      }
    ]
  },
  {
    "title": "Network packet forgery with Scapy",
    "venue": "PacSec/core05",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/scapy_pacsec05.pdf",
      },
      {
        tooltip: "Handout",
        icon: mdiNotebook,
        link: BASE_URL + "talks/scapy_pacsec05.handout.pdf",
      }
    ]
  },
  {
    "title": "Network packet manipulation with Scapy",
    "venue": "Hack.lu 2005",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/scapy_hack.lu.pdf",
      }
    ]
  },
  {
    "title": "Network packet manipulation with Scapy",
    "venue": "Summer school Applied IT 2005",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/scapy_Aachen.pdf",
      }
    ]
  },
  {
    "title": "Scapy: explore the net with new eyes",
    "venue": "T2’2005",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/scapy_T2.pdf",
      }
    ]
  },
  {
    "title": "Packet generation and network based attacks with Scapy",
    "venue": "CanSecWest/core05",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/scapy_csw05.pdf",
      }
    ]
  },
  {
    "title": "Scapy : interactive packet manipulation",
    "venue": "LSM 2003",
    "links": [
      {
        tooltip: "Slides",
        icon: mdiPresentation,
        link: BASE_URL + "talks/scapy_lsm2003.pdf",
      }
    ]
  },
];

/* Naïve OS detection */
function defaultOS() {
  //@ts-ignore
  const platform = (navigator.userAgentData && navigator.userAgentData.platform || navigator.platform).toLowerCase();
  if (platform.includes("win")) return "windows";
  if (platform.includes("linux")) return "linux";
  return "other";
}

/* Download tabs */
import linuxLogo from '@/assets/logos/linux.svg';
import windowsLogo from '@/assets/logos/windows.svg';
import pypiLogo from '@/assets/logos/pypi.svg';
import debianLogo from '@/assets/logos/debian.svg';
import githubLogo from '@/assets/logos/github-mark-white.svg';
import condaLogo from '@/assets/logos/conda.svg';

const dllOS = ref(defaultOS());
const dllMethod = ref("pypi");
const OS = [
  {
    name: "windows",
    logo: windowsLogo,
  },
  {
    name: "linux",
    logo: linuxLogo,
  },
  {
    name: "other",
    text: "?",
  }
];
const METHODS = [
  {
    name: "pypi",
    logo: pypiLogo,
  },
  {
    name: "github",
    logo: githubLogo,
  },
  {
    name: "debian",
    logo: debianLogo,
    condition: "linux",
  },
  {
    name: "conda",
    logo: condaLogo,
  },
];

function getMethods() {
  return METHODS.filter(x => !x.condition || x.condition == dllOS.value);
}

watchEffect(() => {
  if (dllMethod.value == "debian" && dllOS.value != "linux")
    dllMethod.value = "pypi";
})

const INSTRUCTIONS: Record<string, string> = {
  "pypi": "pip install scapy",
  "debian": "sudo apt install python3-scapy",
  "github": "pip install https://github.com/secdev/scapy/archive/refs/heads/master.zip",
  "conda": "conda install -c conda-forge scapy",
};

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
