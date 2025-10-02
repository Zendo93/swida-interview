<!-- src/App.vue -->
<template>
  <div id="app">
    <h1>Transport Order System</h1>

    <!-- Optional navigation links -->
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/create">Create Order</router-link>
    </nav>

    <hr/>

    <!-- Dynamic route content will be rendered here -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* Optional basic styles */
nav a {
  margin-right: 1em;
  text-decoration: none;
  color: #42b983;
}
</style>