// Utilities
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAppStore = defineStore('app', () => {
    const drawer = ref(false)

    const adminView = ref(false)

    return {
        drawer,
        adminView,
    }
})
