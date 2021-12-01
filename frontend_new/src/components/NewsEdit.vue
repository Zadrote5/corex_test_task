<template>
  <q-dialog :modelValue="modelValue" @update:modelValue="$emit('update:modelValue', $event)">
<q-card class='edit-card flex flex-center column'>
  <div class='edit-container flex column'>
    <q-btn @click="$emit('update:modelValue', false)">close</q-btn>
    <q-input filled v-model="$repo.newsItem.title" label="Title"></q-input>
    <q-input filled v-model="$repo.newsItem.content" label="Content"></q-input>
    <q-toggle v-model="$repo.newsItem.is_published" label="Publish"></q-toggle>
    <q-select filled v-model="$repo.newsItem.author" :options="$repo.authorList"
              label="Filled" option-label='name' option-value='id'></q-select>
    <q-select v-model="$repo.newsItem.cities" multiple :options="$repo.cityList"
              label="Filled" option-label='name' option-value='id'></q-select>
    <q-btn v-if='$repo.newsItem.id' @click='saveNews($repo.newsItem)'>Save</q-btn>
    <q-btn v-if='$repo.newsItem.id' color='red' @click='deleteNews($repo.newsItem)'>Delete</q-btn>
    <q-btn v-if='!$repo.newsItem.id' @click='createNews()'>Create</q-btn>
  </div>
</q-card>
  </q-dialog>
</template>

<script lang="ts" setup>
import { News, NewsRaw, store } from 'src/store/store'
import axios, { AxiosResponse } from 'axios'


defineProps({
  modelValue: Boolean,
  item: News
})

const emit = defineEmits(['update:modelValue'])

const deleteNews = async (news: News) => {
  if (store.newsItem !== null) {
    if (news.id) {
      const responseNews: AxiosResponse<NewsRaw> = await axios({
        method: 'delete',
        url: `http://0.0.0.0:8000/news/${news.id}/`,
      })
      emit('update:modelValue', false)
      let index: number = store.newsList.findIndex((el: News) => el.id === news.id)
      store.newsList.splice(index, 1)
      if (responseNews) {
        console.log('success delete!')
      }
    }
  }
}
const createNews = async () => {
  if (store.newsItem !== null) {
    const responseNews: AxiosResponse<NewsRaw> = await axios({
      method: 'post',
      url: 'http://0.0.0.0:8000/news/',
      data: store.newsItem.toJson()
    })
    store.newsItem = new News(responseNews.data)
    emit('update:modelValue', false)
    store.newsList.push(store.newsItem)
  }
}
const saveNews = async (news: News) => {
  if (store.newsItem !== null) {
    if (news.id) {
      const responseNews: AxiosResponse<NewsRaw> = await axios({
        method: 'put',
        url: `http://0.0.0.0:8000/news/${news.id}/`,
        data: store.newsItem.toJson()
      })
      store.newsItem = new News(responseNews.data)
      let index: number = store.newsList.findIndex((el: News) => el.id === news.id)
      store.newsList[index] = store.newsItem
    }
  }
}
</script>

<style scoped>
</style>
