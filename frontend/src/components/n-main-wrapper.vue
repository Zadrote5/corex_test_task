<template>
  <div class="n-main-wrapper">
    <p>{{ title }}</p>
    <n-list></n-list>
    <n-cart></n-cart>
  </div>

</template>

<script>
import nList from "./n-list"
import nCart from "./n-cart"

export default {

  name: "n-main-wrapper",
  components: {
    nList,
    nCart
  },
  props: {},
  data() {
    return {
      title: 'Новостной блог'
    }
  },
  computed: {},
  methods: {},
  watch: {},
  mounted() {

  }
}
</script>

<style scoped>
  .n-main-wrapper {
    flex-direction: column;
    display: flex;
    justify-content: center;
    align-content: center;
    max-width: 900px;
    margin: 0 auto;
  }
</style>