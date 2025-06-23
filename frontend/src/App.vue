<script setup lang="ts">
import { ref } from 'vue'
import UserForm from './components/UserForm.vue'
import UserList from './components/UserList.vue'

const listRef = ref()
function refreshList() {
  if (listRef.value) listRef.value.loadUsers()
}
</script>

<template>
  <h1>User Management</h1>
  <UserForm @created="refreshList" />
  <UserList ref="listRef" />
</template>

<style scoped>
h1 {
  margin-bottom: 1rem;
}
</style>
