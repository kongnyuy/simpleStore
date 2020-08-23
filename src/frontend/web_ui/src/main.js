import Vue from 'vue'
import App from './App.vue'


//data store
import Vuex from 'vuex'
import VueRouter from 'vue-router'

import Vuesax from 'vuesax'
import 'vuesax/dist/vuesax.css'

import router from './router'


Vue.config.productionTip = false
//used
Vue.use(Vuex)
Vue.use(VueRouter)
Vue.use(Vuesax, {
  colors: {
    primary: '#5b3cc4',
    success: 'rgb(23, 201, 100)',
    danger: 'rgb(242, 19, 93)',
    warning: 'rgb(255, 130, 0)',
    dark: 'rgb(36, 33, 69)'
  },
   
})


new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')
