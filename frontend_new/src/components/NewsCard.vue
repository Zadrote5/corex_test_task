<template>
  <q-card class='popup-card flex flex-center column q-pa-lg'>
    <div class='top-block flex row'>
      <div class='news-author'>
        {{$repo.newsItem.author.name}}
      </div>
      <div class='news-cities flex column q-ml-auto q-mb-lg'
           v-for='city in $repo.newsItem.cities' v-bind:key='city.id'>
        <div>{{city.name}}</div>
      </div>
    </div>
    <div class='news-title'>
      {{$repo.newsItem.title}}
    </div>
    <div class='news-content'>
      {{$repo.newsItem.content}}
    </div>

  </q-card>
</template>
<style>
.top-block {
  width: 100%;
}
</style>

<script lang="ts" setup>
import { News } from 'src/store/store'

defineProps({
  item: News
})

</script>
