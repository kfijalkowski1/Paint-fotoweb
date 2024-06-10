<script setup>
import { supabase } from '@/lib/supabaseClient'
import { ref } from 'vue'

const name = ref('')
const surname = ref('')
const email = ref('')
const phone = ref('')
const message = ref('')

const emailRules = [
    (value) => {
        if (value) return true

        return 'E-mail jest wymagany.'
    },
    (value) => {
        if (/.+@.+\..+/.test(value)) return true

        return 'E-mail musi być prawidłowy.'
    },
]

const phoneRules = [
    (value) => {
        if (value) return true

        return 'Numer telefonu jest wymagany'
    },
    (value) => {
        if (
            /^([+]?[\s0-9]+)?(\d{3}|[(]?[0-9]+[)])?([-]?[\s]?[0-9])+$/.test(
                value
            )
        )
            return true

        return 'Numer telefonu musi być prawidłowy.'
    },
]

const nameRules = [
    (value) => {
        if (value) return true

        return 'Imię i nazwisko są wymagane.'
    },
]

const messageRules = [
    (value) => {
        if (value) return true

        return 'Wiadomość jest wymagana.'
    },
]

const valid = ref(false)

const successful = ref(false)

const sendMessage = async () => {
    successful.value = false
    try {
        await supabase.from('messages').insert({
            email: email.value,
            sender_name: name.value,
            sender_surname: surname.value,
            message: message.value,
            phone: phone.value,
        })

        successful.value = true
    } finally {
        name.value = ''
        surname.value = ''
        email.value = ''
        phone.value = ''
        message.value = ''
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
                <span class="text-h3 text-white">Kontakt</span>
            </div>
        </v-img>

        <v-form
            v-model="valid"
            @submit.prevent="sendMessage"
        >
            <div class="d-flex flex-column pa-4">
                <div class="d-flex ga-4">
                    <v-text-field
                        label="Imię"
                        v-model="name"
                        required
                        :rules="nameRules"
                    ></v-text-field>
                    <v-text-field
                        label="Nazwisko"
                        v-model="surname"
                        required
                        :rules="nameRules"
                    ></v-text-field>
                </div>
                <v-text-field
                    label="E-mail"
                    type="email"
                    v-model="email"
                    required
                    :rules="emailRules"
                ></v-text-field>
                <v-text-field
                    label="Numer telefonu"
                    v-model="phone"
                    required
                    :rules="phoneRules"
                ></v-text-field>
                <v-textarea
                    label="Wiadomość"
                    v-model="message"
                    required
                    :rules="messageRules"
                ></v-textarea>

                <v-btn
                    class="flex-grow-1"
                    color="secondary"
                    type="submit"
                    :disabled="!valid"
                >
                    Wyślij wiadomość
                </v-btn>

                <v-sheet
                    v-if="successful"
                    color="green"
                    class="ma-4 pa-4 d-flex justify-center"
                    rounded
                >
                    Wysłano wiadomość!
                </v-sheet>
            </div>
        </v-form>
    </div>
</template>
