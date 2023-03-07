<template>
  <v-app-bar flat>
    <v-app-bar-title>
      Scapy
    </v-app-bar-title>
    <v-btn>
      Download
    </v-btn>
    <v-btn href="https://scapy.readthedocs.io">
      <span class="mr-1">Documentation</span> <v-icon>mdi-open-in-new</v-icon>
    </v-btn>
    <v-btn icon href="https://github.com/secdev/scapy">
      <img :src="githubAsset" height="30" />
    </v-btn>
  </v-app-bar>
</template>

<script lang="ts" setup>
import githubAsset from '@/assets/github-mark-white.svg';
</script>
