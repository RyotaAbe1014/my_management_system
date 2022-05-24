import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import Axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, Axios)

Vue.config.productionTip = false
Vue.prototype.$axios = Axios
Axios.defaults.baseURL = 'http://0.0.0.0:8000' //バックエンド側のIPとポート
Axios.defaults.headers.common['Accept'] = 'application/json'
Axios.defaults.headers.common['Content-Type'] = 'application/json;charset=utf-8'
Axios.defaults.headers.common['Access-Control-Allow-Origin'] = 'http://localhost:8080'
Axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest'

new Vue({
  router,
  vuetify,
  render: h => h(App)
}).$mount('#app')
