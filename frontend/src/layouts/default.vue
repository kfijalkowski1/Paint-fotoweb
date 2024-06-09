<template>
    <v-app>
        <AppHeader />

        <v-main>
            <v-sheet
                :elevation="2"
                class="wrapper"
            >
                <router-view />
            </v-sheet>
        </v-main>

        <AppFooter />
    </v-app>
</template>

<script setup>
//
</script>

<style scoped>
.wrapper {
    max-width: 1000px;
    margin: auto;
    margin-top: 16px;
    margin-bottom: 16px;
}
</style>
