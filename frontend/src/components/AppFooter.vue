<template>
    <v-footer
        height="40"
        app
    >
        <span class="text-caption text-disabled">
            <v-icon
                icon="mdi-camera"
                size="16"
                class="mr-2"
            />

            jan.kowalski@fotoweb.com
        </span>

        <div
            class="text-caption text-disabled"
            style="position: absolute; right: 16px"
        >
            &copy; 2024-{{ new Date().getFullYear() }}
            <span class="d-none d-sm-inline-block">
                Nasza magiczna firma, LLC
            </span>
        </div>
    </v-footer>
</template>
