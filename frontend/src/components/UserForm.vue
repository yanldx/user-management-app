<template>
  <form @submit.prevent="submitForm">
    <input v-model="form.first_name" placeholder="Prénom" />
    <input v-model="form.last_name" placeholder="Nom" />
    <input v-model="form.email" type="email" placeholder="Email" />
    <input v-model="form.password" type="password" placeholder="Mot de passe" />
    <button type="submit">Créer</button>
  </form>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
const emit = defineEmits(['created'])

const form = reactive({
  first_name: '',
  last_name: '',
  email: '',
  password: '',
})

async function submitForm() {
  await fetch('http://localhost:5001/users/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(form),
  })
  emit('created')
  form.first_name = ''
  form.last_name = ''
  form.email = ''
  form.password = ''
}
</script>

<style scoped>
input {
  display: block;
  margin: 6px 0;
  padding: 8px;
  width: 100%;
}
button {
  background-color: green;
  color: white;
  padding: 8px 12px;
  border: none;
  margin-top: 8px;
}
button:hover {
  background-color: darkgreen;
}
</style>
