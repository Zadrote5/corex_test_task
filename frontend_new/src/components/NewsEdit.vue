<template>
  <div class='news-container flex flex-center justify-center' v-if='$repo.newsItem'>
    <q-card class='news-card bg-red-1 q-pa-lg'>
      <q-input v-model='$repo.newsItem.title' label='Title'></q-input>
      <q-input v-model='$repo.newsItem.content' label='Content'></q-input>
      <q- v-model:label='$repo.newsItem.is_published'></q->
      <q-select v-model='$repo.newsItem.author' :options='$repo.authorList'
                option-label='name' label='Author'></q-select>
      <q-select v-model='$repo.newsItem.cities' :options='$repo.cityList'
                option-label='name' label='Cities' multiple></q-select>
      <q-btn @click='saveNews()'>Save</q-btn>
      <q-btn v-if='$repo.newsItem.id' @click='deleteNews()' class='bg-red'>Delete</q-btn>
    </q-card>
  </div>
</template>

<script lang="ts" setup>
import { News, NewsRaw, store } from 'src/store/store'
import axios, { AxiosResponse } from 'axios'
import { onMounted } from 'vue'
import {useRoute} from 'vue-router'
const token = localStorage.getItem('token')
import {useRouter} from 'vue-router'
const router = useRouter()
const route = useRoute()

defineProps({
  modelValue: Boolean,
  item: News
})

const deleteNews = async () => {
  if (store.newsItem !== null) {
    const responseNews: AxiosResponse<NewsRaw> = await axios({
      method: 'delete',
      url: `http://0.0.0.0:8000/news/${store.newsItem.id}/`,
      headers: {
        Authorization: `Token ${token || ''}`
      }
    })
    console.log(responseNews)
    let index = store.newsList.findIndex(el => el.id === store.newsItem.id)
    store.newsList.splice(index, 1)
    await router.replace({name: 'newsList'})
  }
}
const saveNews = async () => {
  if (store.newsItem !== null) {
    if (store.newsItem.id) {
      const responseNews: AxiosResponse<NewsRaw> = await axios({
        method: 'put',
        url: `http://0.0.0.0:8000/news/${store.newsItem.id}/`,
        headers: {
          Authorization: `Token ${token || ''}`
        },
        data: store.newsItem.toJson()
      })
      console.log(responseNews)
    }
    else {
      const responseNews: AxiosResponse<NewsRaw> = await axios({
        method: 'post',
        url: 'http://0.0.0.0:8000/news/',
        headers: {
          Authorization: `Token ${token || ''}`
        },
        data: store.newsItem.toJson()
      })
      console.log(responseNews)
    }
    let index = store.newsList.findIndex(el => el.id === store.newsItem.id)
    store.newsList[index] = store.newsItem
    await router.replace({name: 'newsList'})
  }
}





onMounted(async () => {
  if (!route.params.id) {
    store.newsItem = new News({})
  }
  else  {
    const id = route.params.id.toString()
    console.log(id)
    const responseNews: AxiosResponse<NewsRaw> = await axios({
      method: 'get',
      url: `http://0.0.0.0:8000/news/${id}/`,
      headers: {
        Authorization: `Token ${token || ''}`
      }

    })
    store.newsItem = new News(responseNews.data)
  }
  })
</script>



<style scoped>
.news-container{
  width: 100vw;
  height: 100vh;
}
.news-card {
  width: 400px;
  height: 600px;

}
</style>
