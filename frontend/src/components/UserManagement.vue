<template>
  <div class="user-management">
    <h1 class="mb-4 text-xl font-bold">User Management</h1>
    <form class="space-y-2 mb-6" @submit.prevent="submitForm">
      <div>
        <label class="block text-sm">First Name</label>
        <input v-model="form.first_name" class="border p-1 rounded w-full" />
      </div>
      <div>
        <label class="block text-sm">Last Name</label>
        <input v-model="form.last_name" class="border p-1 rounded w-full" />
      </div>
      <div>
        <label class="block text-sm">Email</label>
        <input v-model="form.email" type="email" class="border p-1 rounded w-full" />
      </div>
      <div>
        <label class="block text-sm">Password</label>
        <input v-model="form.password" type="password" class="border p-1 rounded w-full" />
      </div>
      <button type="submit" class="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700 transition-colors">Create</button>
    </form>

    <table class="w-full table-auto border-collapse">
      <thead>
        <tr class="bg-gray-100">
          <th class="border px-2 py-1 text-left">First</th>
          <th class="border px-2 py-1 text-left">Last</th>
          <th v-if="isAdmin" class="border px-2 py-1 text-left">Email</th>
          <th class="border px-2 py-1 text-left"></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user.id" class="odd:bg-gray-50">
          <td class="border px-2 py-1">{{ user.first_name }}</td>
          <td class="border px-2 py-1">{{ user.last_name }}</td>
          <td v-if="isAdmin" class="border px-2 py-1">{{ user.email }}</td>
          <td class="border px-2 py-1 text-center">
            <button @click="deleteUser(user.id)" class="bg-red-500 text-white px-2 py-1 rounded hover:bg-red-600 transition-colors">
              🗑 Supprimer
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'

interface User {
  id: number
  first_name: string
  last_name: string
  email: string
  password?: string
}

const isAdmin = ref(true)

const form = reactive({
  first_name: '',
  last_name: '',
  email: '',
  password: '',
})

const users = ref<User[]>([])

async function loadUsers() {
  const res = await fetch('http://localhost:5001/users/')
  users.value = await res.json()
}

async function submitForm() {
  await fetch('http://localhost:5001/users/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(form),
  })
  form.first_name = ''
  form.last_name = ''
  form.email = ''
  form.password = ''
  await loadUsers()
}

async function deleteUser(id: number) {
  await fetch(`http://localhost:5001/users/${id}`, { method: 'DELETE' })
  await loadUsers()
}

onMounted(loadUsers)
</script>

<style scoped>
.user-management {
  max-width: 600px;
  margin: 0 auto;
}
button {
  transition: transform 0.1s ease-in-out;
}
button:hover {
  transform: translateY(-2px);
}
</style>

