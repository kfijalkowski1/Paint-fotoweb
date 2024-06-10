<script setup>
const sections = [
    {
        name: 'fotograf',
        cards: [
            { text: 'komunia', src: 'komunia.jpg' },
            { text: 'biznesowe', src: 'biznes.jpg' },
            { text: 'szkolne', src: 'szkolna.jpg' },
            { text: 'śluby', src: 'ślubna.jpg' },
            { text: 'produkty', src: 'produktowa.jpg' },
            { text: 'wydarzenia', src: 'wydarzenia.jpg' },
            { text: 'konferencje', src: 'konferencje.jpg' },
            { text: 'plenerowe', src: 'plenerowa.jpg' },
            { text: 'wiele innych', src: 'wieleinnych.jpg' },
        ],
    },
    {
        name: 'studio',
        cards: [
            { text: 'biznesowe', src: 'biznes.jpg' },
            { text: 'portrety', src: 'portret.jpg' },
            { text: 'ciążowe', src: 'ciążowa.jpg' },
            { text: 'green screen', src: 'greenscreen.jpg' },
            { text: 'nagrania', src: 'nagrania.jpg' },
            { text: 'inne', src: 'inne.jpg' },
        ],
    },
]

const getImage = (path) => {
    return new URL(`/src/assets/${path}`, import.meta.url).href
}
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
            <div class="d-flex flex-wrap justify-space-evenly ga-4">
                <v-card
                    v-for="card in section.cards"
                    :key="card.text"
                    width="300"
                >
                    <v-img
                        height="200px"
                        :src="getImage(card.src)"
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
