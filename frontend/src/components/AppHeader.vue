<script setup>
const links = [
    { text: 'Strona główna', href: '/' },
    { text: 'Oferta', href: '/offer' },
    { text: 'Odbierz zdjęcia', href: '/photos' },
    { text: 'Kontakt', href: '/contact' },
]
</script>
<template>
    <v-app-bar
        :elevation="2"
        color="primary"
    >
        <template v-slot:prepend>
            <v-app-bar-nav-icon
                color="secondary"
                icon="mdi-camera"
            ></v-app-bar-nav-icon>
        </template>

        <v-app-bar-title>Fotoweb</v-app-bar-title>

        <template v-slot:append>
            <v-app-bar-nav-icon
                class="d-md-none"
                color="secondary"
            ></v-app-bar-nav-icon>
            <div class="d-none d-md-flex">
                <v-divider
                    vertical
                    :thickness="2"
                    class="mx-2 border-opacity-75"
                />
                <span
                    v-for="link in links"
                    :key="link.text"
                    class="d-flex flex-grow"
                >
                    <RouterLink
                        :to="link.href"
                        class="text-secondary text-decoration-none"
                        exactActiveClass="font-weight-black"
                    >
                        {{ link.text }}
                    </RouterLink>
                    <v-divider
                        vertical
                        :thickness="2"
                        class="mx-2 border-opacity-75"
                    />
                </span>
            </div>
        </template>
    </v-app-bar>
</template>
