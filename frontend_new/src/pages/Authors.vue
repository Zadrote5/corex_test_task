<template>
  <div class='main-container flex-center flex  column'>
    <div class='title text-h1'>Authors</div>
    <div class='news-container q-pt-lg flex flex-center column '>
      <q-btn class='q-mb-lg'>Add author</q-btn>
      <q-card class='author bordered news-card q-mb-md flex flex-center column'
              v-for='author in $repo.authorList' v-bind:key='author.id'>
        <span class='q-mb-lg'>Name: {{ author.name }}</span>
        <q-btn label='Edit this author' @click="$router.push('/author/'+author.id)"></q-btn>
      </q-card>
      <router-view></router-view>
    </div>


  </div>
</template>

<script lang="ts" setup>
// import { ref } from 'vue'

</script>
<style>

.author-card {
  width: 250px;
  height: 200px;
}
.edit-card {
  width: 800px;
  height: 700px;
}
</style>
