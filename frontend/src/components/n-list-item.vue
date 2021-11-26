<template>
<div class="n-list-item">
<n-cart
v-bind:news="news"
/>



  <p> {{news_data.title}}</p>
  <buttton class="open-popup"
  @click="openPopup"
  >ЧИТАТЬ</buttton>
</div>
</template>

<script>
import NCart from "./n-cart"
export default {

  methods: {
    openPopup(e) {
      e.target.parentNode.querySelector('.n-cart').classList.add('active-popup')
    }
  },
  components: {
  NCart
  },
  name: "n-list-item",
  props: {
    news_data: {
      type: Object,
      default() {
        return {}
      }
    }
  },

  data() {

    return {
      news: this.news_data
    }
  },

}
</script>

<style scoped>
.item-cities {
  margin-left: auto;
}
  .item-title-block {
    display: flex;
    flex-direction: row;
    gap: 4rem;

  }
  .n-list-item:hover {
    background: #f3f3f3;
  }
  .n-list-item {
    padding: 2rem;
    border: beige 1px solid;
    display: flex;
    flex-direction: row;

    gap: 4rem;
  }
  .open-popup {
    margin-left: auto;
    cursor: pointer;
  }
</style>