<script lang="ts" setup>
import { useDisplay } from 'vuetify';
import { watchEffect, onMounted, onBeforeUnmount, ref } from 'vue';
import type { Ref } from 'vue'

const logo_big = `\
                     aSPY//YASa
            apyyyyCY//////////YCa
           sY//////YSpcs  scpCY//Pp
ayp ayyyyyyySCP//Pp           syY//C
AYAsAYYYYYYYY///Ps              cY//S
        pCCCCY//p          cSSps y//Y
        SPPPP///a          pP///AC//Y
             A//A            cyP////C
             p///Ac            sC///a
             P////YCpc           A//A
      scccccp///pSP///p          p//Y
    sY/////////y  caa            S//P
     cayCyayP//Ya               pY/Ya
      sY/PsY////YCc           aC//Yp
        sc  sccaCY//PCypaapyCP//YSs
                spCPY//////YPSps
                    ccaacs
`;

const logo_mini = `\
      .SYPACCCSASYY
P /SCS/CCS        ACS
       /A          AC
     A/PS       /SPPS
        YP        (SC
        SPS/A.      SC
    Y/PACC          PP
     PY*AYC        CAA
          YYCY//SCYP
`;

const logoText = ref('');
const fontSize = ref('1em');
const { smAndDown } = useDisplay();
watchEffect(() => {
        /* Select proper logo based on display size */
        if (smAndDown.value) {
                logoText.value = logo_mini;
                fontSize.value = '0.7em';
        } else {
                logoText.value = logo_big;
                fontSize.value = '1em';
        }
});

/* Computed Scapy logo - shiny effect */
const logo: Ref<string> = ref('');
function calcLogo() {
        /* Function to handle the color of a letter */
        function letterColor() {
                let prb = Math.random();
                if (prb < 0.005) {
                        return '#80d980';  // very light green
                } else if (prb < 0.03) {
                        return '#40c640';  // light green
                } else {
                        return '#00AA00';  // green
                }
        }

        /* Apply color to every letter */
        return logoText.value.split('').map(x => {
                if (x == ' ') {
                        return x;
                } else {
                        return `<span style='color: ${letterColor()}' class='font-weight-bold'>${x}</span>`;
                }
        }).join('');
}

/* Load logo, then refresh again every 100ms */
let interval: ReturnType<typeof setInterval>;
onMounted(() => {
        logo.value = calcLogo();
        interval = setInterval(() => {
                logo.value = calcLogo();
        }, 100);
});
onBeforeUnmount(() => {
        clearInterval(interval);
});
</script>

<template>
        <v-container class="fill-height px-0">
                <!-- Only show arriving animation on bigger screens -->
                <div :class="'text-justify fill-height scapy-logo' + (smAndDown ? ' mini' : '')" v-html="logo">
                </div>
        </v-container>
</template>

<style scoped lang="scss">
/* Whole logo style */
.scapy-logo {
        /* Keep spaces and carriage returns */
        white-space: pre;
        /* Monospace font */
        font-family: Courier New, Courier, Lucida Sans Typewriter, Lucida Typewriter, monospace;
        font-size: v-bind(fontSize);
        /* Animation */
        transition: transform 2s ease-out 100ms;
        animation: zoomInLeft 1s, breath 8s ease-in-out 1s infinite;
}

.scapy-logo.mini {
        animation: breath 8s ease-in-out infinite !important;
}

/* Slight breathing animation */
$normalSize: 0.87;
$beatSize: 0.9;

@keyframes breath {
        0% {
                transform: scale($normalSize);
        }

        25% {
                transform: scale($beatSize);
        }

        50% {
                transform: scale($normalSize);
        }

        75% {
                transform: scale($beatSize);
        }

        100% {
                transform: scale($normalSize);
        }
}

/*!
 * animate.css - https://animate.style/
 * Version - 4.1.1
 * Licensed under the Hippocratic License 2.1 - http://firstdonoharm.dev
 *
 * Copyright (c) 2022 Animate.css
 */
@keyframes zoomInLeft {
        from {
                opacity: 0;
                transform: scale3d(0.1, 0.1, 0.1) translate3d(-1000px, 0, 0);
                animation-timing-function: cubic-bezier(0.55, 0.055, 0.675, 0.19);
        }

        60% {
                opacity: 1;
                transform: scale3d(0.475, 0.475, 0.475) translate3d(10px, 0, 0);
                animation-timing-function: cubic-bezier(0.175, 0.885, 0.32, 1);
        }

        100% {
                transform: scale3d($normalSize, $normalSize, $normalSize);
        }
}
</style>