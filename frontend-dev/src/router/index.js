import { createRouter, createWebHistory} from 'vue-router'
import Login from '@/components/Login'
import Register from "@/components/Register";
import Forget from "@/components/Forget";
import SDChart from "@/components/SDChart";
import Uploadfile from '@/components/Uploadfile'
import ChooseFunc from "@/components/ChooseFunc";
import RFMChart from "@/components/RFMChart";
import TSChart from "@/components/TSChart";

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
  },
  {
    path: '/SDChart',
    component: SDChart
  },
  {
    path: '/uploadfile',
    component: Uploadfile
  },
  {
    path: '/chooseFunc',
    component: ChooseFunc
  },
  {
    path: '/RFMChart',
    component: RFMChart
  },
  {
    path:'/TSChart',
    component: TSChart
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
