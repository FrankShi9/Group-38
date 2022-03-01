import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/components/Login.vue'
import Register from "@/components/Register";

const routes = [
  {
    path: '/',
  },
  {
    path: '/login', 
    component: Login
  },
  {
    path: '/Register',
    component: Register
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
