<template>
    <v-card variant="flat" color="transparent">
        <v-card-text>
            <v-list-item class="px-0" :prepend-avatar="'https://avatars.githubusercontent.com/u/' + props.userid + '?s=80'">
                <v-list-item-title class="text-body-2 text-white">
                    <a :href="'https://github.com/' + props.user" class="text-decoration-none">{{ props.user }}</a>
                </v-list-item-title>
            </v-list-item>
            <iframe :src="'https://github.com/sponsors/' + props.user + '/button'" :title="'Sponsor ' + props.user"
                height="32" width="100%" style="border: 0; border-radius: 6px; filter: invert(80%);">
            </iframe>
        </v-card-text>
    </v-card>
</template>

<script setup lang="ts">
const props = defineProps(['user', 'userid'])
</script>

<style>
/* Don't display different color for visited links */
a,
a:visited {
    color: inherit;
}
</style>