import { createRouter, createWebHistory } from 'vue-router'
import CreateOrder from '../views/CreateOrder.vue'
import OrderList from '../views/OrderList.vue'

const routes = [
  {
    path: '/',
    name: 'OrderList',
    component: OrderList
  },
  {
    path: '/create',
    name: 'CreateOrder',
    component: CreateOrder
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router