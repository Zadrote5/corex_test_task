<template>
  <div class='main-container flex-center flex  column'>
    <div class='title text-h1'>News blog</div>
    <div class='news-container q-pt-lg flex flex-center column '>
      <q-btn class='q-mb-lg' @click="$router.push({name: 'newsCreate'})">Add news</q-btn>
      <q-card class='news bordered news-card q-mb-md flex flex-center column'
              v-for='news in $repo.newsList' v-bind:key='news.id'>
        <span class='q-mb-lg'>{{ news.title }}</span>
        <q-btn label='Open this news' @click="openDialog(news)"></q-btn>
        <q-btn label='Edit this news' @click="$router.push('/news/'+news.id)"></q-btn>
      </q-card>
      <q-dialog v-model='newsDialog'>
        <NewsCard :item='currentNews'></NewsCard>
      </q-dialog>

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
import { ref } from 'vue'
import axios, { AxiosResponse } from 'axios';
import { News, NewsRaw, store } from 'src/store/store';
import NewsCard from 'components/NewsCard.vue'
import NewsEdit from 'components/NewsEdit.vue'


const currentNews = ref<News | null>(null)
const newsDialogEdit = ref(false)
const newsDialog = ref(false)
const token = localStorage.getItem('token')

const openDialog = async (news: News) => {
  if (news.id) {
    const responseNews: AxiosResponse<NewsRaw> = await axios({
      method: 'get',
      url: `http://0.0.0.0:8000/news/${news.id}/`,
      headers: {
        Authorization: `Token ${token || ''}`
      }
    })
    store.newsItem = new News(responseNews.data)
    newsDialog.value = true

  }
}












</script>
