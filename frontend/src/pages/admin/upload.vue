<script setup>
import { supabase } from '@/lib/supabaseClient'
import { useAppStore } from '@/stores/app'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'

const fileInput = ref(null)
const fileSelected = ref(false)

const uuid = ref('')

const onChange = async () => {
    if (fileInput.value.files?.[0]) {
        fileSelected.value = true
    } else {
        fileSelected.value = false
    }
}

const sendFile = async () => {
    uuid.value = ''
    if (fileInput.value.files?.[0]) {
        const file = fileInput.value.files[0]

        const formData = new FormData()
        formData.append('file', file, file.name)
        formData.append('secretKey', 'fhdjslfjdsalk123!')
        const result = await fetch(
            `${import.meta.env.VITE_FILE_SERVER_URL}/upload`,
            {
                method: 'POST',
                body: formData,
            }
        ).then((res) => res.json())

        console.log(result)

        uuid.value = result.uuid

        if (fileInput.value) fileInput.value.value = null
    }
}

const router = useRouter()
const appStore = useAppStore()

onMounted(async () => {
    const data = (await supabase.auth.getSession()).data

    if (!data?.session?.expires_in) {
        router.push('/')
        appStore.adminView = false
    }
})
</script>
<template>
    <div class="pa-4">
        <span class="d-flex justify-center align-center text-h3">
            ADMIN PANEL - UPLOAD FILES
        </span>
    </div>

    <div class="d-flex flex-column align-center">
        <v-btn
            :color="!fileSelected ? 'secondary' : 'success'"
            size="x-large"
            variant="flat"
            tag="label"
        >
            <v-icon
                :icon="!fileSelected ? 'mdi-file' : 'mdi-check'"
                size="large"
                start
            />

            Wybierz plik zip
            <input
                ref="fileInput"
                type="file"
                hidden
                accept=".zip"
                @change="onChange"
            />
        </v-btn>

        <v-btn
            color="primary"
            size="x-large"
            variant="flat"
            :disabled="!fileSelected"
            class="ma-4"
            @click="sendFile"
        >
            Prześlij
        </v-btn>

        <v-text-field
            v-if="uuid"
            :style="{ 'min-width': '400px' }"
            label="Kod dostępu"
            :model-value="uuid"
            readonly
        ></v-text-field>
    </div>
</template>
