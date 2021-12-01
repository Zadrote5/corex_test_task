import { RouteRecordRaw } from 'vue-router';


const routes: RouteRecordRaw[] = [
  {
    path: '/news',
    component: () => import('pages/News.vue'),
    name: 'newsList'
  },
  {
    path: '/',
    component: () => import('pages/Index.vue'),
    name: 'main'
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;
