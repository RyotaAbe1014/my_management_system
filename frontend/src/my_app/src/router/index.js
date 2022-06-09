import Vue from 'vue'
import VueRouter from 'vue-router'
import TopPageView from '../views/TopPageView.vue'
import TagList from '../views/tag/TagList.vue'
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
