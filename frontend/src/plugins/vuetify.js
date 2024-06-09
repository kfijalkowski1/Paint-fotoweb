/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'
// import colors from 'vuetify/util/colors'

const light = {
    dark: false,
    colors: {
        primary: '#A1C6EA',
        secondary: '#7E5A9B',
    },
}

export default createVuetify({
    theme: {
        defaultTheme: 'light',
        themes: {
            light,
        },
    },
})
