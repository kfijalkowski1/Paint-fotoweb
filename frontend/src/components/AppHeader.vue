<script setup></script>
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
            <v-app-bar-nav-icon color="secondary"></v-app-bar-nav-icon>
        </template>
    </v-app-bar>
</template>
