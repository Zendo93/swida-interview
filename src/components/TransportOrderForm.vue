<template>
  <form @submit.prevent="submitForm" class="form-container">
    <div>
      <label>Order Number:</label>
      <input v-model="form.order_number" type="text" required />
    </div>

    <div>
      <label>Customer Name:</label>
      <input v-model="form.customer_name" type="text" required />
    </div>

    <div>
      <label>Date:</label>
      <input v-model="form.date" type="date" required />
    </div>

    <h3>Waypoints</h3>
    <div v-for="(waypoint, index) in form.waypoints" :key="index" class="waypoint">
      <input
        v-model="waypoint.location"
        type="text"
        placeholder="Location"
        required
      />
      <select v-model="waypoint.type" required>
        <option disabled value="">Select Type</option>
        <option value="Pickup">Pickup</option>
        <option value="Delivery">Delivery</option>
      </select>
      <button type="button" @click="removeWaypoint(index)" v-if="form.waypoints.length > 1">
        Remove
      </button>
    </div>

    <button type="button" @click="addWaypoint">Add Waypoint</button>

    <div>
      <button type="submit">Submit Order</button>
    </div>
  </form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import axios from 'axios'

interface Waypoint {
  location: string
  type: 'Pickup' | 'Delivery' | ''
}

interface TransportOrder {
  order_number: string
  customer_name: string
  date: string
  waypoints: Waypoint[]
}
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const form = reactive<TransportOrder>({
  order_number: '',
  customer_name: '',
  date: '',
  waypoints: [
    { location: '', type: '' }
  ]
})

function addWaypoint() {
  form.waypoints.push({ location: '', type: '' })
}

function removeWaypoint(index: number) {
  form.waypoints.splice(index, 1)
}

async function submitForm() {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/orders/`, form)
    console.log('Order submitted successfully:', response.data)
    alert('Order created successfully!')
    // Optionally reset form
  } catch (error) {
    console.error('Error submitting order:', error)
    alert('Failed to submit order.')
  }
}
</script>

<style scoped>
.form-container {
  display: flex;
  flex-direction: column;
  max-width: 500px;
  gap: 1rem;
}
.waypoint {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}
input, select, button {
  padding: 0.5rem;
}
</style>