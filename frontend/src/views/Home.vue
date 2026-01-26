<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <div class="relative bg-slate-900 dark:bg-[#0f172a] text-white overflow-hidden">
        <div class="absolute inset-0 bg-grid-white/[0.05] bg-[length:30px_30px]"></div>
        <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-transparent to-transparent"></div>
        <div class="max-w-[1200px] mx-auto px-6 py-20 relative z-10">
            <div class="max-w-3xl">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 text-blue-400 border border-blue-500/20 text-xs font-bold uppercase tracking-wider mb-6 backdrop-blur-sm">
                    <span class="w-2 h-2 rounded-full bg-blue-400 animate-pulse"></span>
                    Tech & Life
                </div>
                <h1 class="text-5xl md:text-6xl font-black tracking-tight mb-6 font-display leading-tight">
                    探索技术的边界 <br/>
                    <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-400">构建数字世界的未来</span>
                </h1>
                <p class="text-xl text-slate-400 leading-relaxed max-w-2xl">
                    这里汇集了关于全栈开发、系统架构以及前沿技术趋势的深度思考。希望每一行代码，都能成为通往未来的阶梯。
                </p>
            </div>
        </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-6 py-12 -mt-10 relative z-20">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Main Content (Left 8 cols) -->
        <div class="lg:col-span-8">
            
            <!-- Category Filter -->
            <div class="bg-white dark:bg-[#1e293b] rounded-2xl p-2 mb-8 shadow-sm border border-gray-100 dark:border-gray-800 flex items-center">
                <div 
                    ref="categoryScroll"
                    @mousedown="startDrag"
                    @mouseleave="stopDrag"
                    @mouseup="stopDrag"
                    @mousemove="onDrag"
                    class="flex gap-2 overflow-x-auto p-2 scrollbar-hide cursor-grab active:cursor-grabbing select-none w-full"
                >
                    <button
                        v-for="cat in allCategories"
                        ref="categoryItems"
                        :key="cat.slug"
                        @click="setActiveCategory(cat.slug)"
                        class="flex-shrink-0 px-4 py-2 rounded-xl text-sm font-bold transition-all duration-200"
                        :class="[
                            activeCategory === cat.slug
                            ? 'bg-slate-900 text-white shadow-lg shadow-slate-900/20 dark:bg-blue-600 dark:shadow-blue-600/20'
                            : 'bg-transparent text-gray-500 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-800'
                        ]"
                    >
                        {{ cat.name }}
                    </button>
                </div>
                <div class="pl-4 border-l border-gray-100 dark:border-gray-700">
                     <button class="p-2 text-gray-400 hover:text-slate-900 dark:hover:text-white transition-colors">
                        <span class="material-symbols-outlined">search</span>
                     </button>
                </div>
            </div>

            <!-- Loading Skeleton -->
            <div v-if="loading" class="space-y-8">
                <div v-for="i in 3" :key="i" class="bg-white dark:bg-[#1e293b] rounded-3xl p-6 border border-gray-100 dark:border-gray-800 animate-pulse">
                    <div class="h-64 bg-gray-200 dark:bg-gray-700 rounded-2xl mb-6"></div>
                    <div class="h-8 bg-gray-200 dark:bg-gray-700 rounded-lg w-3/4 mb-4"></div>
                    <div class="h-4 bg-gray-200 dark:bg-gray-700 rounded w-full mb-2"></div>
                    <div class="h-4 bg-gray-200 dark:bg-gray-700 rounded w-2/3"></div>
                </div>
            </div>

            <!-- Article List -->
            <div v-else-if="filteredArticles.length" class="space-y-10">
                <!-- Featured Article (First Item) -->
                <article v-if="filteredArticles[0]" class="group relative bg-white dark:bg-[#1e293b] rounded-3xl overflow-hidden shadow-xl shadow-slate-200/50 dark:shadow-none border border-gray-100 dark:border-gray-800 transition-transform duration-300 hover:-translate-y-1">
                     <router-link :to="{ name: 'ArticleDetail', params: { slug: filteredArticles[0].slug } }" class="block relative h-[400px] overflow-hidden">
                        <div class="absolute inset-0 bg-gray-900/30 group-hover:bg-gray-900/20 transition-colors z-10"></div>
                        <img 
                            v-if="filteredArticles[0].cover_image" 
                            :src="filteredArticles[0].cover_image" 
                            class="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-700"
                            alt="Cover"
                        >
                        <div v-else class="w-full h-full bg-gradient-to-br from-blue-500 to-purple-600"></div>
                        
                        <div class="absolute bottom-0 left-0 p-8 z-20 w-full bg-gradient-to-t from-black/80 to-transparent">
                            <span v-if="filteredArticles[0].category" class="inline-block px-3 py-1 rounded-lg bg-blue-500 text-white text-xs font-bold mb-3">
                                {{ filteredArticles[0].category.name }}
                            </span>
                            <h2 class="text-3xl md:text-4xl font-bold text-white mb-3 leading-tight drop-shadow-md">
                                {{ filteredArticles[0].title }}
                            </h2>
                            <div class="flex items-center gap-4 text-gray-300 text-sm font-medium">
                                <span>{{ formatDate(filteredArticles[0].published_at) }}</span>
                                <span class="w-1 h-1 bg-gray-400 rounded-full"></span>
                                <span>{{ filteredArticles[0].view_count || 0 }} 阅读</span>
                            </div>
                        </div>
                     </router-link>
                </article>

                <!-- Regular Articles Grid -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <article 
                        v-for="article in filteredArticles.slice(1)" 
                        :key="article.id" 
                        class="bg-white dark:bg-[#1e293b] rounded-2xl overflow-hidden border border-gray-100 dark:border-gray-800 hover:shadow-lg transition-all duration-300 group flex flex-col h-full"
                    >
                        <router-link :to="{ name: 'ArticleDetail', params: { slug: article.slug } }" class="block h-48 overflow-hidden relative">
                            <div class="absolute top-4 left-4 z-10" v-if="article.category">
                                <span class="px-3 py-1 rounded-full bg-white/90 dark:bg-black/50 backdrop-blur-sm text-xs font-bold text-slate-800 dark:text-white shadow-sm">
                                    {{ article.category.name }}
                                </span>
                            </div>
                            <img 
                                v-if="article.cover_image" 
                                :src="article.cover_image" 
                                class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-500"
                            >
                            <div v-else class="w-full h-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-slate-300">
                                <span class="material-symbols-outlined text-4xl">image</span>
                            </div>
                        </router-link>
                        <div class="p-6 flex-1 flex flex-col">
                            <div class="flex items-center gap-2 text-xs text-gray-400 font-medium mb-3">
                                <span class="material-symbols-outlined text-[14px]">calendar_today</span>
                                {{ formatDate(article.published_at) }}
                            </div>
                            <router-link :to="{ name: 'ArticleDetail', params: { slug: article.slug } }">
                                <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-3 line-clamp-2 group-hover:text-blue-500 transition-colors">
                                    {{ article.title }}
                                </h3>
                            </router-link>
                            <p class="text-gray-500 dark:text-gray-400 text-sm line-clamp-3 mb-4 flex-1">
                                {{ article.summary }}
                            </p>
                            <div class="pt-4 border-t border-gray-100 dark:border-gray-800 flex items-center justify-between">
                                <router-link :to="{ name: 'ArticleDetail', params: { slug: article.slug } }" class="text-sm font-bold text-slate-700 dark:text-gray-300 hover:text-blue-500 flex items-center gap-1 group/btn">
                                    阅读更多 <span class="material-symbols-outlined text-sm transform group-hover/btn:translate-x-1 transition-transform">arrow_forward</span>
                                </router-link>
                            </div>
                        </div>
                    </article>
                </div>
            </div>

            <!-- Empty State -->
            <div v-else class="text-center py-20 bg-white dark:bg-[#1e293b] rounded-3xl border border-dashed border-gray-200 dark:border-gray-700">
                <div class="inline-flex items-center justify-center w-16 h-16 rounded-full bg-gray-50 dark:bg-gray-800 text-gray-400 mb-4">
                    <span class="material-symbols-outlined text-3xl">post_add</span>
                </div>
                <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-1">暂无文章</h3>
                <p class="text-gray-500 dark:text-gray-400">该分类下暂时没有内容，请稍后再来看看。</p>
            </div>

            <!-- Pagination -->
            <div v-if="filteredArticles.length > 5" class="mt-12 flex justify-center">
                 <button class="px-6 py-3 bg-white dark:bg-[#1e293b] border border-gray-200 dark:border-gray-700 rounded-xl text-sm font-bold text-slate-700 dark:text-gray-300 hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors shadow-sm">
                    加载更多文章
                 </button>
            </div>
        </div>

        <!-- Sidebar (Right 4 cols) -->
        <div class="lg:col-span-4 space-y-8">
            
            <!-- Author Profile Widget -->
            <div class="bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 shadow-sm relative overflow-hidden group">
                 <div class="absolute top-0 left-0 w-full h-20 bg-gradient-to-r from-blue-500 to-purple-500 opacity-90"></div>
                 <div class="relative pt-10 px-2 text-center">
                    <div class="w-20 h-20 mx-auto bg-white p-1 rounded-full shadow-lg mb-4">
                        <div class="w-full h-full rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center overflow-hidden">
                             <span class="material-symbols-outlined text-4xl text-gray-400">person</span>
                        </div>
                    </div>
                    <h3 class="text-lg font-bold text-slate-900 dark:text-white">Tech Blogger</h3>
                    <p class="text-sm text-blue-500 font-medium mb-4">Full Stack Developer</p>
                    <p class="text-gray-500 dark:text-gray-400 text-sm mb-6 leading-relaxed">
                        热爱代码，热爱生活。在这里分享我的技术见解和项目实战经验。
                    </p>
                    <div class="flex justify-center gap-3">
                        <a href="#" class="p-2 bg-gray-50 dark:bg-gray-800 rounded-lg hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-blue-500 transition-colors">
                            <span class="material-symbols-outlined text-xl">code</span>
                        </a>
                        <a href="#" class="p-2 bg-gray-50 dark:bg-gray-800 rounded-lg hover:bg-blue-50 dark:hover:bg-blue-900/30 hover:text-blue-500 transition-colors">
                            <span class="material-symbols-outlined text-xl">alternate_email</span>
                        </a>
                    </div>
                 </div>
            </div>

            <!-- Popular Articles -->
            <div class="bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 shadow-sm">
                <div class="flex items-center justify-between mb-6">
                    <h3 class="font-bold text-slate-900 dark:text-white flex items-center gap-2">
                        <span class="material-symbols-outlined text-orange-500">local_fire_department</span>
                        热门文章
                    </h3>
                </div>
                <div class="space-y-4">
                     <div v-for="(article, index) in popularArticles" :key="article.id" class="flex gap-4 group cursor-pointer" @click="$router.push({ name: 'ArticleDetail', params: { slug: article.slug } })">
                        <div class="flex-shrink-0 w-8 text-2xl font-black text-gray-200 dark:text-gray-700 font-display group-hover:text-orange-500/50 transition-colors">
                            {{ String(index + 1).padStart(2, '0') }}
                        </div>
                        <div>
                            <h4 class="text-sm font-bold text-slate-800 dark:text-gray-200 leading-snug mb-1 group-hover:text-blue-500 transition-colors line-clamp-2">
                                {{ article.title }}
                            </h4>
                            <span class="text-xs text-gray-400">{{ article.view_count }} 次阅读</span>
                        </div>
                     </div>
                </div>
            </div>

             <!-- Tags Cloud -->
            <div class="bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 shadow-sm">
                <div class="flex items-center gap-2 mb-6">
                    <span class="material-symbols-outlined text-blue-500">label</span>
                    <h3 class="font-bold text-slate-900 dark:text-white">热门标签</h3>
                </div>
                <div class="flex flex-wrap gap-2">
                    <span 
                        v-for="tag in tags" 
                        :key="tag.id"
                        class="px-3 py-1.5 rounded-lg bg-gray-50 dark:bg-gray-800 text-xs font-medium text-gray-600 dark:text-gray-300 hover:bg-blue-500 hover:text-white dark:hover:bg-blue-500 transition-colors cursor-pointer"
                    >
                        # {{ tag.name }}
                    </span>
                    <span v-if="!tags.length" class="text-sm text-gray-400">暂无标签</span>
                </div>
            </div>

            <!-- Subscribe -->
            <div class="bg-gradient-to-br from-slate-900 to-slate-800 rounded-2xl p-8 text-center text-white relative overflow-hidden">
                <div class="absolute top-0 right-0 w-32 h-32 bg-blue-500/20 rounded-full blur-3xl -mr-10 -mt-10"></div>
                <div class="relative z-10">
                    <div class="inline-flex p-3 rounded-2xl bg-white/10 mb-4 backdrop-blur-sm">
                        <span class="material-symbols-outlined text-2xl">mark_email_unread</span>
                    </div>
                    <h3 class="text-xl font-bold mb-2">订阅更新</h3>
                    <p class="text-slate-300 text-sm mb-6">每周精选技术好文，直接发送到您的邮箱。</p>
                    <button @click="openSubscribeModal" class="w-full py-3 px-4 bg-white text-slate-900 rounded-xl font-bold hover:bg-blue-50 transition-colors shadow-lg">
                        立即订阅 ({{ subscriberCount }})
                    </button>
                </div>
            </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import api from '@/api'
import moment from 'moment'

export default {
  name: 'Home',
  inject: ['openSubscribeModal'],
  data() {
    return {
      articles: [],
      categories: [],
      popularArticles: [],
      tags: [],
      subscriberCount: 0,
      activeCategory: 'all',
      loading: true,
      error: null,
      isDown: false,
      startX: 0,
      scrollLeft: 0
    }
  },
  computed: {
    allCategories() {
      return [{ name: '全部文章', slug: 'all' }, ...this.categories]
    },
    filteredArticles() {
      if (this.activeCategory === 'all') return this.articles
      return this.articles.filter(a => a.category && a.category.slug === this.activeCategory)
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    startDrag(e) {
      this.isDown = true
      this.$refs.categoryScroll.classList.add('cursor-grabbing')
      this.startX = e.pageX - this.$refs.categoryScroll.offsetLeft
      this.scrollLeft = this.$refs.categoryScroll.scrollLeft
    },
    stopDrag() {
      this.isDown = false
      this.$refs.categoryScroll.classList.remove('cursor-grabbing')
    },
    onDrag(e) {
      if (!this.isDown) return
      e.preventDefault()
      const x = e.pageX - this.$refs.categoryScroll.offsetLeft
      const walk = (x - this.startX) * 2 // scroll-fast
      this.$refs.categoryScroll.scrollLeft = this.scrollLeft - walk
    },
    setActiveCategory(slug) {
      if (this.isDown) return
      this.activeCategory = slug
      this.centerActiveCategory(slug)
    },
    centerActiveCategory(slug) {
      const index = this.allCategories.findIndex(c => c.slug === slug)
      if (index === -1 || !this.$refs.categoryItems || !this.$refs.categoryItems[index]) return
      
      const el = this.$refs.categoryItems[index]
      const container = this.$refs.categoryScroll
      
      const elCenter = el.offsetLeft + (el.offsetWidth / 2)
      const containerCenter = container.offsetWidth / 2
      const scrollPos = elCenter - containerCenter - container.offsetLeft
      
      container.scrollTo({
        left: scrollPos,
        behavior: 'smooth'
      })
    },
    async fetchData() {
      this.loading = true
      try {
        const params = {}
        if (this.$route.query.search) {
          params.search = this.$route.query.search
        }
        
        // Parallel requests for better performance
        const [artRes, catRes, popRes, subRes, tagRes] = await Promise.all([
          api.getArticles(params),
          api.getCategories(),
          api.getPopularArticles(),
          api.getSubscriberStats(),
          api.getTags()
        ])
        
        this.articles = artRes.data.results || artRes.data
        this.categories = catRes.data.results || catRes.data
        this.popularArticles = popRes.data
        this.subscriberCount = subRes.data.count
        this.tags = tagRes.data.results || tagRes.data
      } catch (err) {
        this.error = '无法加载内容'
        console.error(err)
      } finally {
        this.loading = false
      }
    },
    formatDate(date) {
      if (!date) return ''
      return moment(date).format('YYYY-MM-DD')
    }
  },
  watch: {
    '$route.query.search'() {
      this.fetchData()
    }
  }
}
</script>

<style scoped>
/* Hide scrollbar for Chrome, Safari and Opera */
.scrollbar-hide::-webkit-scrollbar {
    display: none;
}
/* Hide scrollbar for IE, Edge and Firefox */
.scrollbar-hide {
    -ms-overflow-style: none;  /* IE and Edge */
    scrollbar-width: none;  /* Firefox */
}
</style>