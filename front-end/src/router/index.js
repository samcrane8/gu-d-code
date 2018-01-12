import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  { path: '/', component: 'Shop' },
  { path: '/cart', component: 'Cart' },
  { path: '/about', component: 'About' },
  { path: '/career', component: 'Career'},
  { path: '/sourcing', component: 'Sourcing'},
  { path: '/support', component: 'Support'},
  { path: '/product', component: 'Product'},
  { path: '/checkout', component: 'Checkout'}
]

const routes = routerOptions.map(route => {
  return {
    path: route.path,
    component: () => import(`@/components/${route.component}.vue`)
  }
})

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes
})