import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'jquery/src/jquery.js'
import 'bootstrap/dist/js/bootstrap.min.js'

createApp(App)
    .use(router)
    .use(VueSidebarMenu)
    .mount('#app')