<script setup>
import { ref } from 'vue'

const accessCode = ref('')

const photos = ref([
    { url: 'aaa' },
    { url: 'aaa' },
    { url: 'aaa' },
    { url: 'aaa' },
])

const show = () => {
    // sprawdź dostęp -> może wyświetl błąd
    // pobierz dane
    // wyświetl wszystko
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
                <span class="text-h3 text-white">Odbierz zdjęcia</span>
                <v-btn
                    variant="outlined"
                    color="white"
                >
                    Więcej
                    <v-icon icon="mdi-arrow-down"></v-icon>
                </v-btn>
            </div>
        </v-img>

        <div class="pa-4 d-flex flex-column">
            <v-text-field
                v-model="accessCode"
                label="Kod dostępu"
                required
            ></v-text-field>

            <v-btn
                class="flex-grow-1"
                color="secondary"
                @click="show"
            >
                Otwórz
            </v-btn>
        </div>

        <div
            v-if="photos.length > 0"
            class="pa-4 pt-0 d-flex flex-column"
        >
            <v-divider class="mb-4" />
            <v-btn
                class="flex-grow-1 mb-4"
                color="green"
                @click="downloadAll"
            >
                Pobierz wszystkie
            </v-btn>

            <div class="d-flex flex-wrap justify-space-evenly">
                <v-card
                    v-for="photo in photos"
                    :key="photo.url"
                    width="300"
                >
                    <v-img
                        height="200px"
                        src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
                        cover
                    ></v-img>

                    <template v-slot:actions>
                        <v-btn class="flex-grow-1">Pobierz</v-btn>
                    </template>
                </v-card>
            </div>
        </div>
    </div>
</template>
