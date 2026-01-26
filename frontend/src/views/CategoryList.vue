<template>
  <div class="min-h-screen">
    <!-- Hero Header -->
    <div class="relative bg-slate-900 dark:bg-[#0f172a] text-white overflow-hidden">
      <div class="absolute inset-0 bg-grid-white/[0.05] bg-[length:30px_30px]"></div>
      <div class="absolute inset-0 bg-gradient-to-b from-transparent to-slate-900/50"></div>
      
      <div class="max-w-[1200px] mx-auto px-6 py-20 relative z-10 text-center">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/10 text-white/80 border border-white/20 text-xs font-bold uppercase tracking-wider mb-6 backdrop-blur-sm">
           <span class="w-2 h-2 rounded-full bg-blue-400"></span>
           Collection
        </div>
        <h1 class="text-4xl md:text-5xl font-black tracking-tight mb-4 font-display">
          {{ title }}
        </h1>
        <p v-if="description" class="text-lg text-slate-300 max-w-2xl mx-auto">
            {{ description }}
        </p>
      </div>
    </div>

    <div class="max-w-[1000px] mx-auto px-6 py-12 -mt-10 relative z-20">
      
      <!-- Breadcrumb -->
      <div class="flex items-center gap-2 text-sm text-gray-500 mb-8 bg-white dark:bg-[#1e293b] p-4 rounded-xl shadow-sm border border-gray-100 dark:border-gray-800 w-fit">
        <router-link to="/" class="hover:text-primary transition-colors">首页</router-link>
        <span>/</span>
        <router-link to="/topics" class="hover:text-primary transition-colors">话题</router-link>
        <span>/</span>
        <span class="font-bold text-slate-900 dark:text-white">{{ title }}</span>
      </div>

      <!-- Loading State -->
      <div v-if="loading" class="space-y-6">
        <div v-for="i in 3" :key="i" class="bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 animate-pulse">
            <div class="h-6 w-2/3 bg-gray-200 dark:bg-gray-700 rounded mb-4"></div>
            <div class="h-4 w-full bg-gray-100 dark:bg-gray-800 rounded mb-2"></div>
            <div class="h-4 w-1/2 bg-gray-100 dark:bg-gray-800 rounded"></div>
        </div>
      </div>

      <!-- Article List -->
      <div v-else-if="articles.length" class="space-y-6">
        <article
          v-for="article in articles"
          :key="article.id"
          class="group bg-white dark:bg-[#1e293b] rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-800 hover:border-blue-500/30 dark:hover:border-blue-500/30 transition-all duration-300 shadow-sm hover:shadow-lg hover:-translate-y-1"
        >
          <div class="p-6 md:p-8 flex flex-col md:flex-row gap-6">
            <!-- Optional: Thumbnail if available, otherwise just text layout -->
            <div v-if="article.cover_image" class="w-full md:w-48 h-32 md:h-auto flex-shrink-0 rounded-xl overflow-hidden bg-gray-100 dark:bg-gray-800">
                <img :src="article.cover_image" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500" alt="Cover">
            </div>

            <div class="flex-1 flex flex-col justify-center">
                <div class="flex items-center gap-3 text-xs font-bold text-gray-400 mb-3">
                    <span class="flex items-center gap-1">
                        <span class="material-symbols-outlined text-[14px]">calendar_today</span>
                        {{ formatDate(article.published_at) }}
                    </span>
                    <span v-if="article.category" class="px-2 py-0.5 rounded-md bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400">
                        {{ article.category.name }}
                    </span>
                </div>
                
                <router-link :to="{ name: 'ArticleDetail', params: { slug: article.slug } }">
                    <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-3 group-hover:text-blue-500 transition-colors leading-tight">
                    {{ article.title }}
                    </h3>
                </router-link>
                
                <p class="text-gray-500 dark:text-gray-400 text-sm leading-relaxed line-clamp-2 mb-4">
                    {{ article.summary }}
                </p>

                <div class="mt-auto pt-4 border-t border-gray-100 dark:border-gray-800/50 flex items-center justify-between">
                    <router-link :to="{ name: 'ArticleDetail', params: { slug: article.slug } }" class="inline-flex items-center gap-1 text-sm font-bold text-slate-700 dark:text-slate-300 hover:text-blue-500 transition-colors">
                        阅读全文 <span class="material-symbols-outlined text-sm">arrow_forward</span>
                    </router-link>
                     <div class="flex items-center gap-4 text-xs text-gray-400">
                        <span class="flex items-center gap-1"><span class="material-symbols-outlined text-[14px]">visibility</span> {{ article.view_count || 0 }}</span>
                    </div>
                </div>
            </div>
          </div>
        </article>
      </div>
      
      <!-- Empty State -->
      <div v-else class="text-center py-20 bg-white dark:bg-[#1e293b] rounded-3xl border border-dashed border-gray-200 dark:border-gray-700">
        <div class="inline-flex items-center justify-center w-20 h-20 rounded-full bg-gray-50 dark:bg-gray-800 text-gray-300 mb-6">
            <span class="material-symbols-outlined text-4xl">inbox</span>
        </div>
        <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2">暂时空空如也</h3>
        <p class="text-gray-500 dark:text-gray-400 max-w-sm mx-auto">
            该分类下暂时没有相关文章，这也是一种留白的美。
        </p>
        <router-link to="/topics" class="inline-block mt-8 px-6 py-2.5 bg-slate-900 dark:bg-white text-white dark:text-slate-900 rounded-xl font-bold hover:opacity-90 transition-opacity">
            探索其他话题
        </router-link>
      </div>

    </div>
  </div>
</template>

<script>
import api from '@/api'
import moment from 'moment'

export default {
  name: 'CategoryList',
  data() {
    return {
      articles: [],
      loading: true,
      title: 'Loading...',
      description: ''
    }
  },
  watch: {
    '$route': 'fetchData'
  },
  created() {
    this.fetchData()
  },
  methods: {
    async fetchData() {
      this.loading = true
      const categorySlug = this.$route.params.category
      const tagSlug = this.$route.params.tag
      
      try {
        let params = {}
        if (categorySlug) {
            this.title = '正在加载分类...'
            params.category = categorySlug
            
            // Parallel fetch: articles and metadata
            const [articlesRes, categoryRes] = await Promise.all([
                api.getArticles(params),
                api.getCategory(categorySlug).catch(() => ({ data: { name: categorySlug, description: '' } }))
            ])
            
            this.articles = articlesRes.data.results || articlesRes.data
            this.title = categoryRes.data.name
            this.description = categoryRes.data.description || `查看所有关于 "${categoryRes.data.name}" 的文章`

        } else if (tagSlug) {
            this.title = '正在加载标签...'
            params.tags = tagSlug
            
            const [articlesRes, tagRes] = await Promise.all([
                api.getArticles(params),
                api.getTag(tagSlug).catch(() => ({ data: { name: tagSlug } }))
            ])

            this.articles = articlesRes.data.results || articlesRes.data
            this.title = `#${tagRes.data.name}`
            this.description = `包含标签 "${tagRes.data.name}" 的所有文章`
        } else {
             // Fallback
             const response = await api.getArticles()
             this.articles = response.data.results || response.data
             this.title = '最新文章'
             this.description = '探索所有技术文章'
        }
      } catch (err) {
        console.error(err)
        this.title = '未找到内容'
        this.description = '无法加载请求的内容，请稍后再试。'
      } finally {
        this.loading = false
      }
    },
    formatDate(date) {
        if (!date) return ''
        return moment(date).format('YYYY-MM-DD')
    }
  }
}
</script>

<style scoped>
/* Scoped styles */
</style>