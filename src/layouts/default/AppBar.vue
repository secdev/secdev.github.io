<template>
  <v-app-bar :elevation="1">
    <v-app-bar-title>
      Scapy
    </v-app-bar-title>
    <v-btn :onclick="scrollToDownloads">
      Downloads
    </v-btn>
    <v-btn href="https://scapy.readthedocs.io">
      <span class="mr-1">Doc<span class="hidden-xs">umentation</span></span> <v-icon>mdi-open-in-new</v-icon>
    </v-btn>
    <v-btn icon href="https://github.com/secdev/scapy">
      <img :src="githubAsset" height="30" />
    </v-btn>
  </v-app-bar>
</template>

<script lang="ts" setup>
import githubAsset from '@/assets/github-mark-white.svg';
import { inject } from 'vue'
import type { Ref } from 'vue'

/* Define a function and a reference to scroll to the Downloads section */
const downloads_section = inject<Ref<HTMLDivElement | null>>('downloads_section');
function scrollToDownloads() {
  downloads_section?.value?.scrollIntoView({ behavior: 'smooth' })
}
</script>
