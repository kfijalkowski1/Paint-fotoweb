<script setup>
import { supabase } from '@/lib/supabaseClient'
import { onMounted, ref } from 'vue'
import { useDate } from 'vuetify'

const dateAdapter = useDate()
const events = ref([])

const today = ref(null)

const getSlots = async () => {
    const slots = await supabase.from('slots').select()

    console.log(Date.parse(slots.data[0].start_time), new Date())

    events.value = slots.data.map((slot) => ({
        title: 'Wolny termin',
        start: dateAdapter.startOfDay(new Date(slot.start_time)),
        end: dateAdapter.startOfDay(new Date(slot.end_time)),
        color: 'blue',
        allDay: true,
    }))
}

onMounted(() => {
    getSlots()
})
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
                <span class="text-h3 text-white">Sprawdź termin</span>
            </div>
        </v-img>
        <div class="pa-4">
            <v-calendar
                ref="calendar"
                v-model="today"
                :events="events"
                color="primary"
                type="month"
            ></v-calendar>
        </div>
    </div>
</template>
