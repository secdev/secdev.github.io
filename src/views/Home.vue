<template>
  <div>
    <!-- The animated Scapy logo box -->
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="auto">
          <ScapyS />
        </v-col>
        <v-col md="6" cols="auto">
          <v-fade-transition>
            <v-card v-show="animationOk">
              <v-card-text class="fill-height scapy-main-box text-blue-lighten-2">
                <template v-if="!mini">
                  | <br />
                </template>
                | Welcome to Scapy<br />
                | Version 2.5.0.dev27<br />
                | <br />
                | https://github.com/secdev/scapy<br />
                | <br />
                | Have fun!<br />
                <template v-if="!mini">
                  | <br />
                  | <br />
                  | <br />
                  | <br />
                  | <br />
                </template>
              </v-card-text>
            </v-card>
          </v-fade-transition>
        </v-col>
      </v-row>
      <v-row>
        <!-- What is Scapy -->
        <v-col cols="8">
          <v-card variant="tonal">
            <v-card-title>What is Scapy</v-card-title>
            <v-card-text>
              <p class="pb-2">
                <span class="text-blue">>>></span> A powerful interactive <span class="font-weight-bold">packet manipulation libary</span> written in Python
              </p>
              <p class="pb-2">
                <span class="text-blue">>>></span> Forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests
                and replies, and much more!
              </p>
              <p class="pb-2">
                <span class="text-blue">>>></span> <span class="font-weight-bold">Cross-platform</span>: runs natively on Linux, Windows, OSX and on most
                Unixes with libpcap
              </p>
            </v-card-text>
          </v-card>
        </v-col>
        <v-col cols="4">
          <v-card variant="tonal">
            <v-card-title>Download Scapy</v-card-title>
            <v-card-text class="text-body-2">
              test
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script lang="ts" setup>
import ScapyS from '@/components/ScapyS.vue'

import { useDisplay, } from 'vuetify';
import { watchEffect, ref, onActivated, onMounted } from 'vue';

const animationOk = ref(false);

/* Wait 1s (animation time), then display Home */
onMounted(() => {
  setTimeout(() => {
    animationOk.value = true;
  }, 1000);
});

/* Populate mini property */
const mini = ref(false);
const { mobile } = useDisplay();
watchEffect(() => {
  mini.value = mobile.value;
});
</script>

<style scoped>
.scapy-main-box {
  /* Monospace font */
  font-family: Courier New, Courier, Lucida Sans Typewriter, Lucida Typewriter, monospace;
}
</style>