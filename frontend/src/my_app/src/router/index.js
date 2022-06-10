import Vue from 'vue'
import VueRouter from 'vue-router'
import TopPageView from '../views/TopPageView.vue'
import TagList from '../views/tag/TagList.vue'
import TagCreate from '../views/tag/TagCreate.vue'
import TagDatail from '../views/tag/TagDatail.vue'
import Auth from '../views/auth/Auth.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'TopPage',
    component: TopPageView
  },
  {
    path: '/tag',
    name: 'TagList',
    component: TagList
  },
  {
    path: '/tag/create',
    name: 'TagCreate',
    component: TagCreate
  },
  {
    path: '/tag/:tagId',
    name: 'TagDatail',
    component: TagDatail
  },
  {
    path: '/login',
    name: 'Auth',
    component: Auth
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
