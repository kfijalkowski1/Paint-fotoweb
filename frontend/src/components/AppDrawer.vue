<script setup>
import { useAppStore } from '@/stores/app'
import { computed } from 'vue'
const appStore = useAppStore()

const links = computed(() =>
    appStore.adminView
        ? [
              { text: 'Wiadomości', href: '/admin/messages' },
              { text: 'Wyślij pliki', href: '/admin/upload' },
              { text: 'Wyloguj', href: '/admin/logout' },
          ]
        : [
              { text: 'Strona główna', href: '/' },
              { text: 'Oferta', href: '/offer' },
              { text: 'Odbierz zdjęcia', href: '/photos' },
              { text: 'Sprawdź termin', href: '/check-slot' },
              { text: 'Kontakt', href: '/contact' },
          ]
)
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
