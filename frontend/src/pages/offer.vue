<script setup>
const sections = [
    {
        name: 'fotograf',
        cards: [
            { text: 'komunia' },
            { text: 'biznesowe' },
            { text: 'szkolne' },
            { text: 'śluby' },
            { text: 'produkty' },
            { text: 'wydarzenia' },
            { text: 'konferencje' },
            { text: 'plenerowe' },
            { text: 'wiele innych' },
        ],
    },
    {
        name: 'studio',
        cards: [
            { text: 'biznesowe' },
            { text: 'portrety' },
            { text: 'ciążowe' },
            { text: 'green screen' },
            { text: 'nagrania' },
            { text: 'inne' },
        ],
    },
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
                <span class="text-h3 text-white">Oferta</span>
            </div>
        </v-img>
        <div
            v-for="section in sections"
            :key="section.name"
            class="pa-4"
        >
            <span
                class="d-flex justify-center align-center text-h3 text-uppercase mb-4"
            >
                {{ section.name }}
            </span>
            <div class="d-flex flex-wrap justify-space-between ga-4">
                <v-card
                    v-for="card in section.cards"
                    :key="card.text"
                    width="300"
                >
                    <v-img
                        height="200px"
                        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                        cover
                    ></v-img>

                    <v-card-title class="d-flex text-uppercase justify-center">
                        {{ card.text }}
                    </v-card-title>
                </v-card>
            </div>
        </div>
    </div>
</template>
