<template>
  <div>
    <button @click="loadUsers">Refresh</button>
    <ul data-testid="list">
      <li v-for="user in users" :key="user.id">
        {{ user.first_name }} {{ user.last_name }} - {{ user.email }}
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface User {
  id: number
  first_name: string
  last_name: string
  email: string
}

const users = ref<User[]>([])

async function loadUsers() {
  const res = await fetch('http://localhost:5001/users/')
  users.value = await res.json()
}

onMounted(loadUsers)
defineExpose({ loadUsers })
</script>
