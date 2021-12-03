<template>
  <router-view v-if="ready"></router-view>
</template>
<style>

.news-card {
  width: 250px;
  height: 200px;
}
.edit-card {
  width: 800px;
  height: 700px;
}
</style>

<script lang="ts" setup>
  import {ref, onMounted} from 'vue'
  import {useRouter, useRoute} from 'vue-router'
  import {  authentication } from 'src/store/authentication'
  const router = useRouter()
  const ready = ref(false)
  const route = useRoute()
  import Authors from 'pages/Autors.vue'

  const color = ref('bg-green')

  // отправить запрос на проверку токен


  onMounted(async () => {
    await authentication.me()

    if (authentication.user && route.name === 'auth') {
      await router.replace({
        name: 'main'
      })
    } else if (!authentication.user) {
      await router.replace({
        name: 'auth'
      })
    }
    ready.value = true
  })


</script>
