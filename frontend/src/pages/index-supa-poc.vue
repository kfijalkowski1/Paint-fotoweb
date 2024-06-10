<script setup>
import { ref, onMounted } from 'vue'
import { supabase } from '@/supabase/supabaseClient'

const countries = ref([])

async function getSlots() {
  const { data } = await supabase.from('slots').select()
  countries.value = data
  console.log("aaaaa")
  console.log(data)
}

onMounted(() => {
  getSlots()
})
</script>

<template>
  <ul>
    <li v-for="slot in slots" :key="slot.id">{{ slot.start_time }}</li>
  </ul>
</template>
