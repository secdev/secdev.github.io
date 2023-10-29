<template>
  <v-app>
    <default-bar />

    <default-view />

    <v-footer class="text-center d-flex flex-column">
      <v-breadcrumbs divider="●">
        <v-breadcrumbs-item>Scapy community</v-breadcrumbs-item>
        <v-breadcrumbs-divider />
        <v-breadcrumbs-item>2008-{{ currentYear }}</v-breadcrumbs-item>
        <v-breadcrumbs-divider />
        <v-breadcrumbs-item><a href="https://scapy.net">scapy.net</a></v-breadcrumbs-item>
      </v-breadcrumbs>
      <p>
        This website is published under <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC-BY-SA-2.5</a>
      </p>
    </v-footer>
  </v-app>
</template>

<script lang="ts" setup>
import DefaultBar from './AppBar.vue'
import DefaultView from './View.vue'
import { provide, ref } from 'vue'

/* Declare scrolling pointers */
const downloads_section = ref<HTMLDivElement | null>(null);
provide('downloads_section', downloads_section);

/* Current year */
const currentYear = new Date().getFullYear();
</script>

<style scoped>
/* Don't display different color for visited links */
a,
a:visited {
  color: inherit;
}
</style>

<style>
/* Fix mobile horizontal scrolling */
html,
body {
  overflow-x: hidden;
}
</style>