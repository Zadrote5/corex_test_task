<template class='flex flex-center justify-center'>
  <div class='auth-main flex flex-center column'>
    <q-card-actions class='auth-card bg-red-1
     flex flex-center justify-center q-pa-lg column'>
      <q-input v-model='login' label='login'></q-input>
      <q-input v-model='password' type="password" label='password'></q-input>
      <q-btn class='q-mt-lg' @click='singIn'>Sign in</q-btn>
    </q-card-actions>
  </div>
</template>

<script lang="ts" setup>

import {ref} from 'vue'

const login = ref('')
const password = ref('')

const singIn = () => {
  console.log(login.value)
}

</script>

<style scoped>
  .auth-card {
    width: 450px;
    height: 600px;
  }
  .auth-main {
    width: 100vw;
    height: 100vh;
  }
</style>
