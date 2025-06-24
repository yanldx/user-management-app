<template>
  <form @submit.prevent="submitForm">
    <input v-model="form.firstname" placeholder="Prénom" />
    <input v-model="form.lastname" placeholder="Nom" />
    <input v-model="form.email" type="email" placeholder="Email" />
    <input v-model="form.password" type="password" placeholder="Mot de passe" />
    <input v-model="form.birthdate" type="date" placeholder="Date de naissance" />
    <input v-model="form.city" placeholder="Ville" />
    <input v-model="form.postal_code" placeholder="Code postal" />
    <button type="submit">Créer</button>

    <p v-if="successMessage" class="success">{{ successMessage }}</p>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </form>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { API_BASE_URL } from '../api'

const emit = defineEmits(['created'])

const form = reactive({
  firstname: '',
  lastname: '',
  email: '',
  password: '',
  birthdate: '',
  city: '',
  postal_code: ''
})

const successMessage = ref('')
const errorMessage = ref('')

async function submitForm() {
  try {
    const res = await fetch(`${API_BASE_URL}/users/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })

    if (!res.ok) throw new Error('Erreur API')

    emit('created')
    successMessage.value = '✅ Utilisateur créé avec succès !'
    errorMessage.value = ''
    form.first_name = ''
    form.last_name = ''
    form.email = ''
    form.password = ''
  } catch (err) {
    successMessage.value = ''
    errorMessage.value = '❌ Erreur lors de la création de l’utilisateur.'
  }
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
.success {
  color: green;
  margin-top: 10px;
}
.error {
  color: red;
  margin-top: 10px;
}
</style>
