import { createRouter, createWebHistory} from 'vue-router'
import Login from '@/components/Login.vue'
import Register from "@/components/Register";
import Forget from "@/components/Forget";
import SDChart from "@/components/SDChart";

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
  },
  {
    path: '/Forget',
    component: Forget
  },
  {
    path: '/SDChart',
    component: SDChart
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
