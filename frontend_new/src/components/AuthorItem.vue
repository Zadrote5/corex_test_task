<template>
  <div class='author-container flex flex-center justify-center' v-if='$repo.authorItem'>
    <q-card class='author-card bg-red-1 q-pa-lg'>
      <q-input v-model='$repo.authorItem.name' label='Name'></q-input>
      <q-input v-model='$repo.authorItem.email' label='Content'></q-input>
      <q-btn @click='saveAuthor()'>Save</q-btn>
      <q-btn v-if='$repo.authorItem.id' @click='deleteAuthor()' class='bg-red'>Delete</q-btn>
    </q-card>
  </div>
</template>

<script>




import { Author, AuthorRaw, store } from '../store/store'
import axios, { AxiosResponse } from 'axios'
import {useRoute} from 'vue-router'
import { onMounted } from 'vue'

const route = useRoute()
const token = localStorage.getItem('token')

console.log('nhfhngfhg')

onMounted(async () => {
  if (!route.params.id) {
    store.authorItem = new Author({})
    console.log('zopa')
  }
  else  {

    const id = route.params.id.toString()
    console.log(id)
    const responseAuthor = await axios({
      method: 'get',
      url: `http://0.0.0.0:8000/author/${id}/`,
      headers: {
        Authorization: `Token ${token || ''}`
      }

    })
    store.authorItemItem = new Author(responseAuthor.data)


  }
})
</script>

<style scoped>
.author-container{
  width: 100vw;
  height: 100vh;
}
.author-card {
  width: 400px;
  height: 600px;

}
</style>
