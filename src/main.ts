import { createApp } from 'vue'

import '@/styles/main.scss'

import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

import App from '@/App.vue'
import router from './router'

createApp(App).use(ElementPlus).use(router).mount('#app')
