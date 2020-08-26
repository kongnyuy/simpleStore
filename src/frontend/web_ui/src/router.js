
import VueRouter from 'vue-router'

import Articles from './components/shop/Articles'
import Shop from './components/shop'
import Inventory from './components/admin/Inventory'
// 0. If using a module system (e.g. via vue-cli), import Vue and VueRouter
// and then call `Vue.use(VueRouter)`.


// 2. Define some routes
// Each route should map to a component. The "component" can
// either be an actual component constructor created via
// `Vue.extend()`, or just a component options object.
// We'll talk about nested routes later.
const routes = [    
    {path: '/articles', component: Articles},
    {path: '/shelfs', component: Shop},
    {path: '/inventory', component: Inventory}
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = new VueRouter({
    routes // short for `routes: routes`
})

// 4. Create and mount the root instance.
// Make sure to inject the router with the router option to make the
// whole app router-aware.

export default router
export {routes}