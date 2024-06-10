<script setup>
import { supabase } from '@/lib/supabaseClient'
import { useAppStore } from '@/stores/app'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const messages = ref([])

const loadMessages = async () => {
    messages.value = (await supabase.from('messages').select()).data.reverse()
}

const deleteMessage = async (id) => {
    await supabase.from('messages').delete().eq('message_id', id)

    await loadMessages()
}

onMounted(() => {
    loadMessages()
})

const router = useRouter()
const appStore = useAppStore()

onMounted(async () => {
    const data = (await supabase.auth.getSession()).data

    if (!data?.session?.expires_in) {
        router.push('/')
        appStore.adminView = false
    } else {
        appStore.adminView = true
    }
})
</script>
<template>
    <div class="pa-4">
        <span class="d-flex justify-center align-center text-h3">
            ADMIN PANEL - WIADOMOŚCI
        </span>

        <div>
            <v-sheet
                elevation="2"
                class="ma-4 pa-2"
                v-for="message in messages"
                :key="message.message_id"
            >
                <div class="d-flex">
                    <div>
                        <p class="text-h5 mx-4">
                            {{ message.sender_name }}
                            {{ message.sender_surname }}
                        </p>
                        <p class="text-caption mx-4">
                            {{ message.email }}
                        </p>
                        <p class="text-caption mx-4">
                            {{ message.phone }}
                        </p>
                    </div>
                    <div class="flex-grow-1" />
                    <div>
                        <v-btn
                            icon="mdi-delete"
                            color="red"
                            @click="deleteMessage(message.message_id)"
                        ></v-btn>
                    </div>
                </div>
                <v-textarea
                    :model-value="message.message"
                    hide-details
                    readonly
                ></v-textarea>
            </v-sheet>
        </div>
    </div>
</template>
