<template>
  <div class='flex flex-center justify-center items-center'>
  <div v-if='check_auth===true'>
    <q-btn :to="{name: 'newsList'}">news</q-btn>
  </div>
    <q-btn v-else :to="{name: 'auth'}">Go to auth page?</q-btn>
  </div>
</template>
<style>

</style>
<script lang="ts" setup>
import axios from 'axios';
import { store } from 'src/store/store';


const check_auth = async () => {
  if (store.auth_token) {
    const responseCheck = await axios({
      method: 'post',
      url: 'http://3196-178-68-38-88.ngrok.io/users/check_token',
      headers: `Authorization: 'Token ${store.auth_token.toString()}'`
    })
    return responseCheck.status == 201;
  }
  else return false
}
</script>
