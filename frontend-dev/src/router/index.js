import { createRouter, createWebHistory} from 'vue-router'
import Login from '@/components/Login'
import Register from "@/components/Register";
import Forget from "@/components/Forget";
import SDChart from "@/components/SDChart";
import Uploadfile from '@/components/Uploadfile'
import ChooseFunc from "@/components/ChooseFunc";
import RFMChart from "@/components/RFMChart";
import TSChart from "@/components/TSChart";
import Waiting from "@/components/Waiting";
import Model from "@/components/Model";
import Admin from "@/components/Admin";
import AboutUs from "@/components/AboutUs";
import Guidance from "@/components/Guidance";
import History from '@/components/History';

const routes = [
  {
    path: '',
    redirect: '/home'
  },
  {
    path: '/home',
    component: ChooseFunc
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
    path: '/RFMChart',
    component: RFMChart
  },
  {
    path:'/TSChart',
    component: TSChart
  },
  {
    path: '/Waiting',
    component: Waiting
  },
  {
    component: Model
  },
  {
    path:'/Admin',
    component: Admin
  },
  {
    path: '/AboutUs',
    component: AboutUs
  },
  {
    path: '/guidance',
    component: Guidance
  },
  {
    path: '/history',
    component: History
  },
  {
    path: '/logout',
    redirect: '/home'
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
