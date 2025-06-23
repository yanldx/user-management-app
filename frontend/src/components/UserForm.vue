<template>
  <form @submit.prevent="submitForm">
    <div>
      <label>First Name</label>
      <input data-testid="first" v-model="form.first_name" placeholder="First name" />
    </div>
    <div>
      <label>Last Name</label>
      <input data-testid="last" v-model="form.last_name" placeholder="Last name" />
    </div>
    <div>
      <label>Email</label>
      <input data-testid="email" v-model="form.email" type="email" placeholder="Email" />
    </div>
    <div>
      <label>Password</label>
      <input data-testid="password" v-model="form.password" type="password" placeholder="Password" />
    </div>
    <button data-testid="submit" type="submit">Create User</button>
  </form>
</template>

<script setup lang="ts">
import { reactive } from 'vue'

const emitSubmit = defineEmits(['created'])

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
  emitSubmit('created')
  form.first_name = ''
  form.last_name = ''
  form.email = ''
  form.password = ''
}
</script>
