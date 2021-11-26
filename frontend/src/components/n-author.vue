<template>
<div class="n-author">
{{name}}
</div>
</template>

<script>
import axios from "axios";


export default {
  props: {
    author: {
      type: Number,
      default() {
        return 0
      }
    }
  },

  data() {
    return {
      name: null
    }
  },
  mounted() {
    axios
        .get('http://0.0.0.0:8000/author/'+ this.author, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        })
        .then(response => (this.name = response.data.name));
  }
}
</script>

<style scoped>

</style>