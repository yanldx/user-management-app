<template>
  <ul>
    <li v-for="user in users" :key="user.id">
      {{ user.first_name }} {{ user.last_name }}
      <span v-if="isAdmin"> - {{ user.email }}</span>
      <button v-if="isAdmin" @click="deleteUser(user.id)">Supprimer</button>
    </li>
  </ul>
</template>

<script setup lang="ts">
const props = defineProps<{ users: any[]; isAdmin: boolean }>()
const emit = defineEmits(['deleted'])

import { API_BASE_URL } from '../api'

async function deleteUser(id: number) {
  await fetch(`${API_BASE_URL}/users/${id}`, { method: 'DELETE' })
  emit('deleted')
}
</script>

<style scoped>
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 6px 0;
  border-bottom: 1px solid #ccc;
}
button {
  margin-left: 10px;
  background-color: red;
  color: white;
  padding: 4px 8px;
  border: none;
}
button:hover {
  background-color: darkred;
}
</style>
