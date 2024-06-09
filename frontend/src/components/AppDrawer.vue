<script setup>
import { useAppStore } from '@/stores/app'
const appStore = useAppStore()

const links = [
    { text: 'Strona główna', href: '/' },
    { text: 'Oferta', href: '/offer' },
    { text: 'Odbierz zdjęcia', href: '/photos' },
    { text: 'Kontakt', href: '/contact' },
]
</script>
<template>
    <v-navigation-drawer
        temporary
        v-model="appStore.drawer"
        location="right"
    >
        <v-list-item
            v-for="link in links"
            :key="link.text"
            link
            :title="link.text"
            :to="link.href"
        ></v-list-item>
    </v-navigation-drawer>
</template>
