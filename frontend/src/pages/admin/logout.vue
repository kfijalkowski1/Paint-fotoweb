<script setup>
import { supabase } from '@/lib/supabaseClient'
import { useAppStore } from '@/stores/app'
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const appStore = useAppStore()

onMounted(async () => {
    await supabase.auth.signOut()

    router.push('/')
    appStore.adminView = false
})
</script>
<template>
    <div></div>
</template>
