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
    </div>
</template>

<script setup>
//
</script>
