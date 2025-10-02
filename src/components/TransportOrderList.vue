<template>
  <div class="transport-order-list">
    <h2>Transport Orders</h2>

    <!-- Filters -->
    <div class="filters">
      <input
        v-model="filters.customer"
        placeholder="Filter by Customer Name"
      />
      <input
        v-model="filters.date"
        type="date"
      />
    </div>

    <!-- Orders Table -->
    <table>
      <thead>
        <tr>
          <th>Order Number</th>
          <th>Customer Name</th>
          <th>Date</th>
          <th>Waypoints</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in filteredOrders" :key="order.orderNumber">
          <td>{{ order.orderNumber }}</td>
          <td>{{ order.customerName }}</td>
          <td>{{ order.date }}</td>
          <td>
            <ul>
              <li v-for="(wp, idx) in order.waypoints" :key="idx">
                {{ wp.location }} ({{ wp.type }})
              </li>
            </ul>
        </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts" setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

interface TransportOrderApi {
  id: number
  order_number: string
  customer_name: string
  date: string
  waypoints?: string[] // Optional, if your API includes this
}

// Define a TypeScript interface for transport orders
interface TransportOrder {
  id: number
  orderNumber: string
  customerName: string
  date: string // ISO format e.g., "2025-10-01"
  waypoints?: string[]
}

const fetchOrders = async () => {
  try {
    const response = await axios.get<TransportOrderApi[]>(`${API_BASE_URL}/api/orders/`)
    orders.value = response.data.map((apiOrder): TransportOrder => ({
      id: apiOrder.id,
      orderNumber: apiOrder.order_number,
      customerName: apiOrder.customer_name,
      date: apiOrder.date,
      waypoints: apiOrder.waypoints || [] // Optional
    }))
  } catch (error) {
    console.error('Failed to fetch orders:', error)
  }
}

const orders = ref<TransportOrder[]>([])

onMounted(() => {
  fetchOrders()
})

// Define the filter object with types
const filters = ref<{
  customer: string
  date: string
}>({
  customer: '',
  date: ''
})

// Filtered orders computed based on inputs
const filteredOrders = computed(() => {
  return orders.value.filter(order => {
    const matchesCustomer = order.customerName
      .toLowerCase()
      .includes(filters.value.customer.toLowerCase())
    const matchesDate =
      !filters.value.date || order.date === filters.value.date

    return matchesCustomer && matchesDate
  })
})
</script>

<style scoped>
.transport-order-list {
  max-width: 800px;
  margin: auto;
  padding: 20px;
}

.filters {
  display: flex;
  gap: 10px;
  margin-bottom: 15px;
}

input {
  padding: 6px 10px;
  font-size: 14px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

thead {
  background-color: #f2f2f2;
}

th, td {
  border: 1px solid #ccc;
  padding: 10px;
  text-align: left;
}
</style>
