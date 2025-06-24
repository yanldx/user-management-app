<template>
  <form @submit.prevent="submit">
    <h2 class="text-xl font-bold mb-4">Login</h2>
    <input v-model="email" type="email" placeholder="Your email" class="border p-2 w-full rounded mb-2" />
    <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded">Login</button>
  </form>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits<{
  (e: 'login', email: string): void
}>()

const email = ref('')

function submit() {
  emit('login', email.value.trim())
}
</script>
