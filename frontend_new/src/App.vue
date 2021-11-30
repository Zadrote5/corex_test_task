<template>
  {{$repo.authorList}}
  <br/>
  {{$repo.countryList}}
  <br/>
  {{$repo.cityList}}
  <br/>
  {{$repo.newsList}}
</template>
<script lang="ts" setup>
import {onMounted} from 'vue'
import axios, { AxiosResponse } from 'axios';
import { Author, AuthorRaw, City, CityRaw, Country, CountryRaw, News, NewsRaw, store } from 'src/store/store';


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
