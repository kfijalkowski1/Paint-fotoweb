<script setup>
const sections = [
    { title: 'AAAAA', text: 'BBBBBB' },
    { title: 'AAAAB', text: 'BBBBBB' },
    { title: 'AAAAC', text: 'BBBBBB' },
]
</script>
<template>
    <div>
        <v-img
            :width="1000"
            :max-height="300"
            aspect-ratio="16/9"
            cover
            src="@/assets/cover.jpg"
        >
            <div
                class="d-flex flex-column ga-8 align-center justify-center fill-height"
            >
                <span class="text-h3 text-white">Fotoweb</span>
                <v-btn
                    variant="outlined"
                    color="white"
                >
                    Więcej
                    <v-icon icon="mdi-arrow-down"></v-icon>
                </v-btn>
            </div>
        </v-img>
        <span class="d-flex justify-center align-center text-h3 ma-4">
            O NAS
        </span>

        <div
            :class="{ 'flex-md-row-reverse': index % 2 }"
            class="d-flex flex-column flex-md-row my-4"
            v-for="(section, index) in sections"
            :key="section.title"
        >
            <v-img
                height="400px"
                max-width="500px"
                src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                cover
            ></v-img>
            <div
                class="pa-4 flex-grow-1"
                :class="{ 'text-end': index % 2 !== 1 }"
            >
                <h5 class="text-h5">AAAAAAAAA</h5>
                <p>BBBBB {{ index }}</p>
            </div>
        </div>
    </div>
</template>
