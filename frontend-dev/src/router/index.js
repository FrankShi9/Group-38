import { createRouter, createWebHistory} from 'vue-router'
import Login from '@/components/Login.vue'
import Register from "@/components/Register";
import Forget from "@/components/Forget";

const routes = [
  {
    path: '/',
  },
  {
    path: '/login', 
    component: Login
  },
  {
    path: '/register',
    component: Register
  },
  {
    path: '/forget',
    component: Forget
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
