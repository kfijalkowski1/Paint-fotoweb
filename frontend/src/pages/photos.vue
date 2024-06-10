<script setup>
import { ref } from 'vue'

const accessCode = ref('')

const photos = ref([])
const allPhotos = ref('')
const errorMessage = ref('')

const show = async () => {
    photos.value = []
    allPhotos.value = ''
    errorMessage.value = ''

    try {
        const fileList = await fetch(
            `${import.meta.env.VITE_FILE_SERVER_URL}/getFileList/${
                accessCode.value
            }`
        ).then((data) => data.json())

        const zipFileName = fileList.find((file) =>
            file.match(/^.*\.(zip|ZIP)$/)
        )

        allPhotos.value =
            zipFileName &&
            `${import.meta.env.VITE_FILE_SERVER_URL}/files/${
                accessCode.value
            }/${zipFileName}`

        photos.value = fileList
            .filter((file) => !file.match(/^.*\.(zip|ZIP)$/))
            .map((file) => ({
                url: `${import.meta.env.VITE_FILE_SERVER_URL}/files/${
                    accessCode.value
                }/${file}`,
            }))
    } catch {
        errorMessage.value = 'Ten kod dostępu jest nieprawidłowy'
    }
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
            </div>
        </v-img>

        <div class="pa-4 d-flex flex-column">
            <v-text-field
                v-model="accessCode"
                label="Kod dostępu"
                required
                :error="errorMessage !== ''"
                :error-messages="errorMessage"
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
                v-if="allPhotos"
                class="flex-grow-1 mb-4"
                color="green"
                download
                :href="allPhotos"
            >
                Pobierz wszystkie
            </v-btn>

            <div class="d-flex flex-wrap justify-space-evenly ga-4">
                <v-card
                    v-for="photo in photos"
                    :key="photo.url"
                    width="300"
                >
                    <v-img
                        height="200px"
                        :src="photo.url"
                        cover
                    ></v-img>

                    <template v-slot:actions>
                        <v-btn
                            class="flex-grow-1"
                            download
                            :href="photo.url"
                        >
                            Pobierz
                        </v-btn>
                    </template>
                </v-card>
            </div>
        </div>
    </div>
</template>
