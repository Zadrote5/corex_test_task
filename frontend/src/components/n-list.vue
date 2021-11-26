<template>
  <div class="n-list">
    <h1>{{ title }}</h1>

    <n-list-item
      v-for="one_news in news"
      :key="one_news.id"
      v-bind:news_data="one_news"
    />
    <n-cart/>

  </div>
</template>

<script>
  import nListItem from "./n-list-item"
  import axios from "axios";


  export default {

  name: "n-list",
  props:{},
  data() {
    return {
      news: null,
      title: 'Список новостей'
    }
  },


    mounted() {
    axios
        .get('http://0.0.0.0:8000/news.json', {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
          })
        .then(response => (this.news = response.data));
  },
  components: {
    nListItem
  },
  computed: {}
}
</script>

<style scoped>
  .n-list {
    display: flex;
    flex-direction: column;
    gap: 2rem;

  }
</style>