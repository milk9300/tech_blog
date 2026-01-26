import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/Home.vue')
    },
    {
        path: '/topics',
        name: 'Topics',
        component: () => import('../views/Topics.vue')
    },
    {
        path: '/category/:category',
        name: 'CategoryList',
        component: () => import('../views/CategoryList.vue')
    },
    {
        path: '/tag/:tag',
        name: 'TagList',
        component: () => import('../views/CategoryList.vue')
    },
    {
        path: '/article/:slug',
        name: 'ArticleDetail',
        component: () => import('../views/ArticleDetail.vue')
    },
    {
        path: '/about',
        name: 'About',
        component: () => import('../views/About.vue')
    }

]

const router = new VueRouter({
    mode: 'history',
    base: import.meta.env.BASE_URL,
    routes
})

export default router
