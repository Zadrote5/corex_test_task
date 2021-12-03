<template>
  <q-layout view="lHh Lpr lFf">

    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>

          Quasar App
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      bordered
      class='flex column'
    >
      <q-btn :to="{name: 'newsList'}">News</q-btn>
      <q-btn :to="{name: 'authorList'}">Authors</q-btn>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>
<style>

</style>
<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import axios, { AxiosResponse } from 'axios'
import { Author, AuthorRaw, City, CityRaw, Country, CountryRaw, News, NewsRaw, store } from 'src/store/store'
const leftDrawerOpen = ref(false)
const loadAuthors = async () => {
  const token = localStorage.getItem('token')

  const responseAuthors: AxiosResponse<AuthorRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/author/',
    headers: {
      Authorization: `Token ${token || ''}`
    }
  })
  store.authorList = responseAuthors.data.map((val: AuthorRaw) => new Author(val))

  const responseCountry: AxiosResponse<CountryRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/country/',
    headers: {
      Authorization: `Token ${token || ''}`
    }
  })
  store.countryList = responseCountry.data.map((val: CountryRaw) => new Country(val))

  const responseCity: AxiosResponse<CityRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/city/',
    headers: {
      Authorization: `Token ${token || ''}`
    }
  })
  store.cityList = responseCity.data.map((val: CityRaw) => new City(val))

  const responseNews: AxiosResponse<NewsRaw[]> = await axios({
    method: 'get',
    url: 'http://0.0.0.0:8000/news/',
    headers: {
      Authorization: `Token ${token || ''}`
    }
  })
  store.newsList = responseNews.data.map((val: NewsRaw) => new News(val))
}
onMounted(() => {
  void loadAuthors()


})
</script>
