<script setup>
import { supabase } from '@/lib/supabaseClient'
import { useAppStore } from '@/stores/app'
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import { useDate } from 'vuetify'

const dateAdapter = useDate()
const events = ref([])

const today = ref(null)

const getSlots = async () => {
    const slots = await supabase.from('slots').select()

    const availableDays = slots.data.map((slot) => ({
        date: new Date(slot.start_time),
        id: slot.visit_id,
    }))

    let newEvents = []

    let currentDay = dateAdapter.startOfDay(new Date())
    for (let i = 0; i < 30; i++) {
        const day = availableDays.find((date) =>
            dateAdapter.isSameDay(date.date, currentDay)
        )
        if (day) {
            newEvents.push({
                title: 'Usuń termin',
                start: dateAdapter.startOfDay(new Date(currentDay)),
                end: dateAdapter.startOfDay(new Date(currentDay)),
                color: 'red',
                allDay: true,
                addSlot: false,
                id: day.id,
            })
        } else {
            newEvents.push({
                title: 'Dodaj termin',
                start: dateAdapter.startOfDay(new Date(currentDay)),
                end: dateAdapter.startOfDay(new Date(currentDay)),
                color: 'green',
                allDay: true,
                addSlot: true,
            })
        }

        currentDay = dateAdapter.addDays(currentDay, 1)
    }

    events.value = newEvents
}

const addSlot = async (day) => {
    const date = day.date

    await supabase.from('slots').insert({
        start_time: dateAdapter.toISO(dateAdapter.addHours(date, 1)),
        end_time: dateAdapter.toISO(dateAdapter.addHours(date, 23)),
        is_reserved: false,
    })

    getSlots()
}

const removeSlot = async (id) => {
    await supabase.from('slots').delete().eq('visit_id', id)

    getSlots()
}

onMounted(() => {
    getSlots()
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
            ADMIN PANEL - MESSAGE LIST
        </span>

        <div class="pa-4">
            <v-calendar
                ref="calendar"
                v-model="today"
                :events="events"
                color="primary"
                type="month"
            >
                <template #event="{ allDay, event, day }">
                    <VChip
                        :color="event.color"
                        density="comfortable"
                        :label="allDay"
                        :style="{ width: '100%' }"
                        @click="
                            event.addSlot ? addSlot(day) : removeSlot(event.id)
                        "
                    >
                        <VBadge
                            inline
                            dot
                            :color="event.color"
                        />

                        {{ event.title }}
                    </VChip>
                </template>
            </v-calendar>
        </div>
    </div>
</template>
