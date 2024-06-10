<script setup>
import { supabase } from '@/lib/supabaseClient'
import { useAppStore } from '@/stores/app'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')

const router = useRouter()
const appStore = useAppStore()

const authorize = async () => {
    try {
        await supabase.auth.signInWithPassword({
            email: email.value,
            password: password.value,
        })

        router.push('/admin/messages')
        appStore.adminView = true
    } catch {
        email.value = ''
        password.value = ''
    }
}

onMounted(async () => {
    const data = (await supabase.auth.getSession()).data

    if (data?.session?.expires_in) {
        router.push('/admin/messages')
        appStore.adminView = true
    }
})
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
                v-model="email"
                label="E-mail"
                type="email"
                required
            ></v-text-field>
            <v-text-field
                v-model="password"
                label="Hasło"
                type="password"
                required
                hidden
            ></v-text-field>

            <v-btn
                class="flex-grow-1"
                color="secondary"
                @click="authorize"
            >
                Zaloguj
            </v-btn>
        </div>
    </div>
</template>
