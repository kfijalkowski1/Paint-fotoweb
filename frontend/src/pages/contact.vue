<script setup>
import { ref } from 'vue'

const name = ref('')
const email = ref('')
const message = ref('')

const successful = ref(false)

const sendMessage = () => {
    // sprawdź dane
    // wyślij wiadomość
    // wyświetl potwierdzenie i wyczyść pola
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
                <span class="text-h3 text-white">Kontakt</span>
            </div>
        </v-img>

        <div class="d-flex flex-column pa-4">
            <v-text-field
                label="Imię i Nazwisko"
                v-model="name"
                required
            ></v-text-field>
            <v-text-field
                label="Email"
                type="email"
                v-model="email"
                required
            ></v-text-field>
            <v-textarea
                label="Wiadomość"
                v-model="message"
                required
            ></v-textarea>

            <v-btn
                class="flex-grow-1"
                color="secondary"
                @click="sendMessage"
            >
                Wyślij wiadomość
            </v-btn>
        </div>
    </div>
</template>
