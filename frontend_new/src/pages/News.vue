<template>
  <div class='main-container flex-center flex  column'>
    <div class='title text-h1'>News blog</div>
    <div class='news-container q-pt-lg flex flex-center column '>
      <q-btn class='q-mb-lg' @click="$router.push({name: 'newsCreate'})">Add news</q-btn>
      <q-card class='news bordered news-card q-mb-md flex flex-center column'
              v-for='news in $repo.newsList' v-bind:key='news.id'>
        <span class='q-mb-lg'>{{ news.title }}</span>
        <q-btn label='Edit this news' @click="$router.push('/news/'+news.id)"></q-btn>
      </q-card>
      <router-view></router-view>
    </div>


  </div>
</template>
<style>

.news-card {
  width: 250px;
  height: 200px;
}
.edit-card {
  width: 800px;
  height: 700px;
}
</style>

<script lang="ts" setup>



</script>
