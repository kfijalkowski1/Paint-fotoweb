<script setup>
import { ref } from 'vue'

const login = ref('')
const password = ref('')

const authorize = () => {
    // send request to database
    // if correct redirect
}
</script>
<template>
    <div>
        <span class="d-flex justify-center align-center text-h3">
            ADMIN PANEL
        </span>

        <div
            class="pa-4 ma-auto d-flex flex-column"
            :style="{ 'max-width': '500px' }"
        >
            <v-text-field
                v-model="login"
                label="Login"
                required
            ></v-text-field>
            <v-text-field
                v-model="password"
                label="Password"
                required
                hidden
            ></v-text-field>

            <v-btn
                class="flex-grow-1"
                color="secondary"
                @click="authorize"
            >
                Login
            </v-btn>
        </div>
    </div>
</template>
