import Vue from 'vue'
import VueRouter from 'vue-router'
import TopPageView from '../views/TopPageView.vue'
import TagList from '../views/tag/TagList.vue'
import TagCreate from '../views/tag/TagCreate.vue'
import TagDatail from '../views/tag/TagDatail.vue'
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
