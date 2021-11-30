<template>
  <div class="n-cart">
    <div class="close-btn" @click="closePopup">
      &times;
    </div>
    <div class="popup-content">
      <div class="popup-top-block">
        <div class="author">
          <n-author v-bind:author_id="news_data.author"/>
        </div>
        <div class="cities">
          <n-city v-for="city in news_data.cities"
                  :key="city"
                  v-bind:city_id="city"
          />
        </div>
      </div>
      <div class="popup-title">
        {{news_data.title }}
      </div>
      <div class="popup-content">
        {{news_data.content }}
      </div>
    </div>
  </div>

</template>

<script>
import nCity from './n-city'
import nAuthor from './n-author'
import axios from "axios";
export default {
  components: {
    nCity,
    nAuthor
  },
  methods: {
    closePopup(e) {
     e.target.parentNode.classList.remove('active-popup')
    }
  },
  name: "n-cart",
  props:{
    news_id: {
      type: Number,
      default() {
        return 0
      }
    }
  },
  data() {
    return {
      news_data: {},
    }
  },
  mounted() {
    axios
        .get('http://0.0.0.0:8000/news/'+ this.news_id, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        .then(response => (this.news_data = response.data));
  },
  computed: {}

}
</script>

<style scoped>
  .n-cart {
    display: none;
    position: fixed;
    z-index: 999;
    width: 100vw;
    height: 100vw;
    background-color: rgba(51, 48, 48, 0.3);

    left: 0;
    top: 0;
    padding-top: 5rem;
    justify-content: center;
  }
  .active-popup {
    display: flex !important;
  }
  .popup-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 70vw;
    height: 70vh;
    background-color: rgba(255, 255, 255, 1);
    padding-top: 4rem;
  }
  .popup-title {
    max-width: 90%;
    font-size: 4rem;
  }
  .popup-top-block {
    display: flex;
    flex-direction: row;
    width: 90%;
  }
  .cities {
    font-size: 0.8rem ;
    margin-left: auto;
  }
  .close-btn {
    position: absolute;
    right: 5rem;
    top: 2rem;
    font-size: 5rem;
    cursor: pointer;
  }
  .popup-content {
    max-width: 90%;
    font-size: 2rem;
  }
</style>