import Vue from 'vue'
import Router from 'vue-router'
import programManage from '@/components/programManage'
import Home from '@/components/Home'
import BuscarPorFecha from '@/components/BuscarPorFecha'
import Login from '@/components/Login'
import PlanEstudio from '@/components/PlanEstudio'
import HomeAdmin from '@/components/HomeAdmin'
import VerPrograma from '@/components/VerPrograma'
import BuscarPorFechaAdmin from '@/components/BuscarPorFechaAdmin'
import MenuPrograma from '@/components/MenuPrograma'
import AsignarPrograma from '@/components/asignarPrograma'
import ProgramAsigned from '@/components/programAsigned'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/programManage',
      name: 'programManage',
      component: programManage,
      props: true
    },
    {
      path: '/home',
      name: 'Home',
      component: Home,
      props: true
    },
    {
      path: '/homeAdmin',
      name: 'HomeAdmin',
      component: HomeAdmin,
      props: true
    },
    {
      path: '/buscar',
      name: 'BuscarPorFecha',
      component: BuscarPorFecha,
      props: true
    },
    {
      path: '/buscarAdmin',
      name: 'BuscarPorFechaAdmin',
      component: BuscarPorFechaAdmin,
      props: true
    },
    {
      path: '/planEstudio',
      name: 'PlanEstudio',
      component: PlanEstudio,
      props: true
    },
    {
      path: '/verPrograma',
      name: 'verPrograma',
      component: VerPrograma,
      props: true
    },
    {
      path: '/menuPrograma',
      name: 'MenuPrograma',
      component: MenuPrograma,
      props: true
    },
    {
      path: '/asignarPrograma',
      name: 'asignarPrograma',
      component: AsignarPrograma,
    },
    {
      path: '/programaAsignado',
      name: 'progamAsigned',
      component: ProgramAsigned,
      props: true
    }
  ]
})
