<template>
  <div>
    <router-link :to="{name: 'newsList'}">
      news
    </router-link>
    <q-btn :to="{name: 'newsList'}">news</q-btn>
  </div>
</template>
<style>

</style>
<script lang="ts">
import { LocalStorage } from 'quasar'
import axios, { AxiosResponse } from 'axios';

function check_auth () {
  if (LocalStorage.has('auth_token')) {
    let token = LocalStorage.getItem('auth_token')

  }
}
</script>
