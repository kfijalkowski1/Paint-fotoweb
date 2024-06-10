<script setup>
const sections = [
    {
        title: 'Studio',
        text: 'Nasze studio fotograficzne oferuje profesjonalne sesje zdjęciowe w przyjaznej i komfortowej atmosferze.  Dysponujemy nowoczesnym sprzętem i kreatywnym zespołem, który uwieczni najważniejsze chwile w Twoim życiu.  Zapraszamy do współpracy zarówno osoby prywatne, jak i firmy, gwarantując najwyższą jakość usług i satysfakcję z efektów.',
        src: 'studio.jpg',
    },
    {
        title: 'Fotografia',
        text: 'Nasze usługi fotograficzne obejmują szeroki zakres, od sesji portretowych i rodzinnych, przez fotografię ślubną, aż po zdjęcia korporacyjne i produktowe.  Każde zlecenie traktujemy indywidualnie, dbając o detale i dostosowując styl zdjęć do oczekiwań klienta. Gwarantujemy profesjonalne podejście, kreatywność oraz wysoką jakość końcowych fotografii.',
        src: 'portret.jpg',
    },
    {
        title: 'Zespół',
        text: 'Adam Jeliński, Bartosz Pełka, Krzysztof Fijałkowski i Rafał Szczepaniak',
        src: 'zespół.jpg',
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
            class="d-flex flex-column flex-md-row my-4 align-center"
            v-for="(section, index) in sections"
            :key="section.title"
        >
            <div class="flex-grow-1">
                <v-img
                    height="400px"
                    width="400px"
                    :src="'/src/assets/' + section.src"
                    cover
                ></v-img>
            </div>
            <div
                class="pa-4 flex-grow-1"
                :style="{ 'max-width': '600px' }"
            >
                <h5 class="text-h5">{{ section.title }}</h5>
                <p>{{ section.text }}</p>
            </div>
        </div>
    </div>
</template>
