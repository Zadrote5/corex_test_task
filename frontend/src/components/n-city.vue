<template>
<div class="n-city">
  {{name}}
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "n-city",
  props: {
    city_id: {
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
        .get('http://0.0.0.0:8000/city/'+ this.city_id, {
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