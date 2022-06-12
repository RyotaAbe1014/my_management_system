import Vue from 'vue'
import VueRouter from 'vue-router'
import TopPageView from '../views/TopPageView.vue'
import TagList from '../views/tag/TagList.vue'
import TagCreate from '../views/tag/TagCreate.vue'
import TagDatail from '../views/tag/TagDatail.vue'
import Auth from '../views/auth/Auth.vue'
import CreateReport from '../views/daily_report/CreateReport.vue'
import ReportList from '../views/daily_report/ReportList.vue'
import TargetList from '../views/target_management/TargetList.vue'
import CreateTarget from '../views/target_management/CreateTarget.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'Auth',
    component: Auth
  },
  {
    path: '/',
    name: 'TopPage',
    component: TopPageView,
    meta: { requiresAuth: true }
  },
  {
    path: '/tag',
    name: 'TagList',
    component: TagList,
    meta: { requiresAuth: true }
  },
  {
    path: '/tag/create',
    name: 'TagCreate',
    component: TagCreate,
    meta: { requiresAuth: true }
  },
  {
    path: '/tag/:tagId',
    name: 'TagDatail',
    component: TagDatail,
    meta: { requiresAuth: true }
  },
  {
    path: '/daily_report/create',
    name: 'CreateReport',
    component: CreateReport,
    meta: { requiresAuth: true }
  },
  {
    path: '/daily_report/',
    name: 'ReportList',
    component: ReportList,
    meta: { requiresAuth: true }
  },
  {
    path: '/target/',
    name: 'TargetList',
    component: TargetList,
    meta: { requiresAuth: true }
  },
  {
    path: '/target/create',
    name: 'CreateTarget',
    component: CreateTarget,
    meta: { requiresAuth: true }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

// ログイン判定
router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth)

  if (requiresAuth) {
    const user = sessionStorage.getItem('user')
    console.log(user)
    if (!user) {
      next({
        path: '/login',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else {
    next()
  }
})



export default router
