import { RouteRecordRaw } from 'vue-router';


const routes: RouteRecordRaw[] = [

  {
    path: '/',
    redirect: {name: 'newsList'},
    component: () => import('pages/Index.vue'),
    name: 'main',
    children: [
      {
        path: 'news',
        component: () => import('pages/News.vue'),
        name: 'newsList',

      },
      {
        path: 'news/:id',
        component: () => import('components/NewsEdit.vue'),
        name: 'newsItem'
      },
      {
        path: 'news/create',
        component: () => import('components/NewsEdit.vue'),
        name: 'newsCreate'
      }

    ]
  },
  {
    path: '/auth',
    component: () => import('components/authPage.vue'),
    name: 'auth'
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue'),
  },
];

export default routes;
