<template>
  <div class="container">
    <h1>User Management</h1>

    <div v-if="!isAdmin && !showLogin">
      <UserForm @created="loadUsers" />
      <button @click="showLogin = true">Accès administrateur</button>
    </div>

    <div v-if="showLogin && !isAdmin">
      <h2>Connexion admin</h2>
      <input v-model="loginEmail" type="email" placeholder="Email admin" />
      <input v-model="loginPassword" type="password" placeholder="Mot de passe" />
      <button @click="login">Connexion</button>
      <button @click="showLogin = false">Annuler</button>
      <p v-if="error" class="error">{{ error }}</p>
    </div>

    <div v-if="isAdmin">
      <p><strong>Connecté en tant qu’admin</strong></p>
      <button @click="logout">Se déconnecter</button>
      <UserForm @created="loadUsers" />
      <UserList :users="users" :isAdmin="true" @deleted="loadUsers" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { API_BASE_URL } from '../api'
import UserForm from './UserForm.vue'
import UserList from './UserList.vue'

const isAdmin = ref(false)
const showLogin = ref(false)
const loginEmail = ref('')
const loginPassword = ref('')
const error = ref('')
const users = ref([])

async function loadUsers() {
  const res = await fetch(`${API_BASE_URL}/users/`)
  users.value = await res.json()
}

async function login() {
  try {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: loginEmail.value,
        password: loginPassword.value,
      }),
    })

    if (!response.ok) throw new Error()

    const data = await response.json()
    localStorage.setItem('token', data.access_token)
    isAdmin.value = true
    showLogin.value = false
    error.value = ''
    loadUsers()
  } catch {
    error.value = 'Identifiants incorrects'
  }
}

function logout() {
  isAdmin.value = false
  loginEmail.value = ''
  loginPassword.value = ''
  users.value = []
  localStorage.removeItem('token')
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: auto;
  font-family: Arial, sans-serif;
  padding: 20px;
}
input {
  display: block;
  margin: 6px 0;
  padding: 8px;
  width: 100%;
}
button {
  margin-top: 8px;
  padding: 8px 12px;
  background-color: #007bff;
  border: none;
  color: white;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}
.error {
  color: red;
  margin-top: 10px;
}
</style>
