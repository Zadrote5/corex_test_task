<template>
  <div class='main-container flex-center flex  column'>
    <div class='title text-h1'>News blog</div>
    <div class='news-container q-pt-lg flex flex-center column '>
      <q-btn class='q-mb-lg' @click='openDialogAdd()'>Add news</q-btn>
      <q-card class='news bordered news-card q-mb-md flex flex-center column'
              v-for='news in $repo.newsList' v-bind:key='news.id'>
        <span class='q-mb-lg'>{{ news.title }}</span>
        <q-btn label='Open this news' @click="openDialog(news)"></q-btn>
        <q-btn label='Edit this news' @click="openDialogEdit(news)"></q-btn>
      </q-card>
      <q-dialog v-model='newsDialog'>
          <NewsCard :item='currentNews'></NewsCard>
      </q-dialog>
        <NewsEdit :item='currentNews' v-model='newsDialogEdit'></NewsEdit>
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
import {onMounted, ref} from 'vue'
import axios, { AxiosResponse } from 'axios';
import { Author, AuthorRaw, City, CityRaw, Country, CountryRaw, News, NewsRaw, store } from 'src/store/store';
import NewsCard from 'components/NewsCard.vue'
import NewsEdit from 'components/NewsEdit.vue'

const currentNews = ref<News | null>(null)
const newsDialog = ref(false)
const newsDialogEdit = ref(false)

const openDialog = async (news: News) => {
  if (news.id) {
    const responseNews: AxiosResponse<NewsRaw> = await axios({
      method: 'get',
      url: `http://0.0.0.0:8000/news/${news.id}/`
    })
    store.newsItem = new News(responseNews.data)

    newsDialog.value = true
  }
}
const openDialogEdit = async (news: News) => {
  if (news.id) {
    const responseNews: AxiosResponse<NewsRaw> = await axios({
      method: 'get',
      url: `http://0.0.0.0:8000/news/${news.id}/`
    })
    store.newsItem = new News(responseNews.data)
    newsDialogEdit.value = true
  }
}

function openDialogAdd () {

  store.newsItem = new News({})
  newsDialogEdit.value = true
}

const loadAuthors = async () => {

  const responseAuthors: AxiosResponse<AuthorRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/author/'
  })
  store.authorList = responseAuthors.data.map((val: AuthorRaw) => new Author(val))

  const responseCountry: AxiosResponse<CountryRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/country/'
  })
  store.countryList = responseCountry.data.map((val: CountryRaw) => new Country(val))

  const responseCity: AxiosResponse<CityRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/city/'
  })
  store.cityList = responseCity.data.map((val: CityRaw) => new City(val))

  const responseNews: AxiosResponse<NewsRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/news/'
  })
  store.newsList = responseNews.data.map((val: NewsRaw) => new News(val))
}



onMounted(() => {
  void loadAuthors()


})


</script>
