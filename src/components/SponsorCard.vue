<template>
    <v-card variant="flat" color="transparent">
        <v-card-text>
            <v-list-item class="px-0" :prepend-avatar="!xs ? UserImageLink : undefined">
                <v-list-item-media v-if="xs">
                    <v-icon>
                        <v-img :src="UserImageLink"></v-img>
                    </v-icon>
                </v-list-item-media>
                <v-list-item-title class="text-body-2 text-white">
                    <a :href="'https://github.com/' + props.user" class="text-decoration-none"><span class="d-none d-lg-inline">{{ props.name }} (</span>@{{ props.user }}<span class="d-none d-lg-inline">)</span></a>
                </v-list-item-title>
                <v-list-item-subtitle>
                    {{ props.role }}
                </v-list-item-subtitle>
            </v-list-item>
            <iframe :src="'https://github.com/sponsors/' + props.user + '/button'" :title="'Sponsor ' + props.user"
                height="32" width="100%" style="border: 0; border-radius: 6px; filter: invert(80%);">
            </iframe>
        </v-card-text>
    </v-card>
</template>

<script setup lang="ts">
import { useDisplay } from 'vuetify';
import { computed } from 'vue';

const props = defineProps(['user', 'userid', 'name', 'role']);
const { xs } = useDisplay();

const UserImageLink = computed(() => {
    return 'https://avatars.githubusercontent.com/u/' + props.userid + '?s=80';
});
</script>

<style>
/* Don't display different color for visited links */
a,
a:visited {
    color: inherit;
}
</style>