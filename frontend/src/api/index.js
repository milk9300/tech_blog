import axios from 'axios'
const api = axios.create({
    baseURL: import.meta.env.VITE_DEBUG === 'true'
        ? import.meta.env.VITE_API_URL_LOCAL
        : import.meta.env.VITE_API_URL_ONLINE,
    timeout: 5000
})

export default {
    getArticles(params) {
        return api.get('/articles/', { params })
    },
    getArticle(slug) {
        return api.get(`/articles/${slug}/`)
    },
    getCategories() {
        return api.get('/categories/')
    },
    getCategory(slug) {
        return api.get(`/categories/${slug}/`)
    },
    getTags() {
        return api.get('/tags/')
    },
    getTag(slug) {
        return api.get(`/tags/${slug}/`)
    },
    subscribe(email) {
        return api.post('/subscribers/', { email })
    },
    getPopularArticles() {
        return api.get('/articles/popular/')
    },
    getSubscriberStats() {
        return api.get('/subscribers/stats/')
    }
}
