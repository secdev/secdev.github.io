<template>
  <v-app>
    <default-bar />

    <default-view />
  </v-app>
</template>

<script lang="ts" setup>
import DefaultBar from './AppBar.vue'
import DefaultView from './View.vue'
import { provide, ref } from 'vue'

/* Declare scrolling pointers */
const downloads_section = ref<HTMLDivElement | null>(null);
provide('downloads_section', downloads_section);
</script>
