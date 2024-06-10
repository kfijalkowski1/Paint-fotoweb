<script setup>
import { ref } from 'vue'
import { useDate } from 'vuetify'

const dateAdapter = useDate()
const events = [
    {
        title: 'test',
        start: dateAdapter.startOfDay(new Date()),
        end: dateAdapter.startOfDay(new Date()),
        color: 'green',
        allDay: true,
    },
]

const today = ref(null)
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
                <span class="text-h3 text-white">Fotoweb</span>
                <v-btn
                    variant="outlined"
                    color="white"
                >
                    Więcej
                    <v-icon icon="mdi-arrow-down"></v-icon>
                </v-btn>
            </div>
        </v-img>
        <div class="pa-4">
            <span class="d-flex justify-center align-center text-h3">
                SPRAWDŹ TERMIN
            </span>

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
