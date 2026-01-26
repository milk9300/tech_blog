<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <div class="relative bg-slate-900 dark:bg-[#0f172a] text-white overflow-hidden">
      <div class="absolute inset-0 bg-grid-white/[0.05] bg-[length:30px_30px]"></div>
      <div class="absolute inset-0 bg-gradient-to-b from-slate-900 via-transparent to-transparent"></div>
      
      <div class="max-w-[1200px] mx-auto px-6 pt-20 pb-24 relative z-10 text-center">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-500/10 text-purple-400 border border-purple-500/20 text-xs font-bold uppercase tracking-wider mb-6 backdrop-blur-sm">
           <span class="w-2 h-2 rounded-full bg-purple-400 animate-pulse"></span>
           Knowledge Base
        </div>
        <h1 class="text-4xl md:text-6xl font-black tracking-tight mb-6 font-display leading-tight">
          探索 <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-400">知识的经纬</span>
        </h1>
        <p class="text-xl text-slate-400 leading-relaxed max-w-2xl mx-auto mb-10">
          从宏观架构到微观代码，这里汇聚了不同维度的技术思考。
        </p>

        <!-- Search Bar -->
        <div class="max-w-xl mx-auto relative group">
            <div class="absolute -inset-1 bg-gradient-to-r from-purple-600 to-pink-600 rounded-xl blur opacity-25 group-hover:opacity-75 transition duration-1000 group-hover:duration-200"></div>
            <div class="relative flex items-center bg-white dark:bg-slate-800 rounded-xl p-2 shadow-2xl">
                <span class="material-symbols-outlined text-gray-400 ml-3">search</span>
                <input 
                    v-model="searchQuery" 
                    type="text" 
                    placeholder="搜索感兴趣的话题或分类..." 
                    class="w-full bg-transparent border-none focus:ring-0 outline-none text-slate-900 dark:text-white placeholder-gray-400 h-10"
                >
            </div>
        </div>
      </div>
    </div>

    <div class="max-w-[1200px] mx-auto px-6 py-12 -mt-10 relative z-20">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <!-- Main Content (Left 8 cols) -->
        <div class="lg:col-span-8 space-y-12">
            
            <!-- Categories Section -->
            <section>
                <div class="flex items-center gap-3 mb-6">
                    <div class="p-2 rounded-lg bg-blue-500/10 text-blue-500">
                        <span class="material-symbols-outlined">category</span>
                    </div>
                    <h2 class="text-2xl font-bold text-slate-900 dark:text-white font-display">核心分类</h2>
                </div>

                <!-- Loading Skeleton -->
                <div v-if="loadingCategories" class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div v-for="i in 4" :key="i" class="h-32 bg-gray-100 dark:bg-gray-800 rounded-2xl animate-pulse"></div>
                </div>

                <!-- Empty State -->
                <div v-else-if="filteredCategories.length === 0" class="text-center py-12 border border-dashed border-gray-200 dark:border-gray-800 rounded-2xl">
                    <p class="text-gray-500">没有找到匹配的分类</p>
                </div>

                <!-- Category List -->
                <div v-else class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <router-link
                        v-for="cat in filteredCategories"
                        :key="cat.id"
                        :to="{ name: 'CategoryList', params: { category: cat.slug } }"
                        class="group relative bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 hover:border-blue-500/30 dark:hover:border-blue-500/30 transition-all duration-300 hover:shadow-lg hover:shadow-blue-500/5 hover:-translate-y-1 overflow-hidden"
                    >
                        <div class="absolute top-0 right-0 p-6 opacity-5 transform translate-x-4 -translate-y-4 group-hover:scale-110 transition-transform duration-500">
                             <span class="material-symbols-outlined text-8xl text-slate-900 dark:text-white">folder_open</span>
                        </div>

                        <div class="relative z-10">
                            <div class="w-12 h-12 rounded-xl bg-gradient-to-br from-blue-50 to-blue-100 dark:from-blue-900/20 dark:to-blue-800/20 flex items-center justify-center text-blue-600 dark:text-blue-400 font-bold text-xl mb-4 group-hover:scale-110 transition-transform duration-300 shadow-inner">
                                {{ cat.name.charAt(0).toUpperCase() }}
                            </div>
                            <h3 class="text-xl font-bold text-slate-900 dark:text-white mb-2 group-hover:text-blue-500 transition-colors">
                                {{ cat.name }}
                            </h3>
                            <p class="text-sm text-gray-500 dark:text-gray-400 line-clamp-2 mb-4 h-10 leading-relaxed">
                                {{ cat.description || '探索该分类下的所有精选文章。' }}
                            </p>
                            <div class="flex items-center justify-between text-xs font-medium text-gray-400 group-hover:text-blue-500/70 transition-colors">
                                <span>{{ cat.articles_count || 0 }} 篇文章</span>
                                <span class="material-symbols-outlined text-lg transform group-hover:translate-x-1 transition-transform">arrow_forward</span>
                            </div>
                        </div>
                    </router-link>
                </div>
            </section>

            <!-- Tags Section -->
            <section>
                 <div class="flex items-center gap-3 mb-6">
                    <div class="p-2 rounded-lg bg-green-500/10 text-green-500">
                        <span class="material-symbols-outlined">label</span>
                    </div>
                    <h2 class="text-2xl font-bold text-slate-900 dark:text-white font-display">热门标签</h2>
                </div>

                <div v-if="loadingTags" class="flex flex-wrap gap-3">
                    <div v-for="i in 10" :key="i" class="h-8 w-20 bg-gray-100 dark:bg-gray-800 rounded-lg animate-pulse"></div>
                </div>

                <div v-else-if="filteredTags.length === 0" class="text-center py-8 text-gray-500">
                    没有找到匹配的标签
                </div>

                <div v-else class="bg-white dark:bg-[#1e293b] rounded-3xl p-8 border border-gray-100 dark:border-gray-800 shadow-sm relative overflow-hidden">
                     <div class="flex flex-wrap gap-3 relative z-10">
                        <router-link
                            v-for="tag in filteredTags"
                            :key="tag.id"
                            :to="{ name: 'TagList', params: { tag: tag.slug } }"
                            class="group relative inline-flex items-center gap-2 px-4 py-2 rounded-xl text-sm font-bold transition-all duration-200 border"
                            :class="[
                                'bg-slate-50 dark:bg-slate-800/50 border-slate-100 dark:border-slate-700 text-slate-600 dark:text-slate-300 hover:bg-slate-900 hover:border-slate-900 hover:text-white dark:hover:bg-blue-600 dark:hover:border-blue-600 dark:hover:text-white hover:shadow-md'
                            ]"
                        >
                            <span class="opacity-50 text-xs">#</span>
                            {{ tag.name }}
                        </router-link>
                     </div>
                </div>
            </section>
        </div>

        <!-- Sidebar (Right 4 cols) -->
        <div class="lg:col-span-4 space-y-8">
            <!-- Stats Widget -->
            <div class="bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 shadow-sm">
                <div class="flex items-center gap-2 mb-6">
                    <span class="material-symbols-outlined text-orange-500">analytics</span>
                    <h3 class="font-bold text-slate-900 dark:text-white">全站统计</h3>
                </div>
                
                <div class="grid grid-cols-2 gap-4">
                    <div class="p-4 rounded-2xl bg-orange-50 dark:bg-orange-500/10 text-center">
                        <div class="text-3xl font-black text-orange-500 mb-1">{{ categories.length }}</div>
                        <div class="text-xs font-bold text-orange-400/80 uppercase">分类</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-blue-50 dark:bg-blue-500/10 text-center">
                        <div class="text-3xl font-black text-blue-500 mb-1">{{ tags.length }}</div>
                        <div class="text-xs font-bold text-blue-400/80 uppercase">标签</div>
                    </div>
                </div>

                <div class="mt-8">
                     <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">内容分布</h4>
                     <div class="space-y-4">
                        <div v-for="(cat, idx) in sortedCategories.slice(0, 5)" :key="cat.id">
                             <div class="flex justify-between text-sm mb-1.5">
                                <span class="font-medium text-slate-700 dark:text-gray-300">{{ cat.name }}</span>
                                <span class="text-xs text-gray-400">{{ cat.articles_count }}</span>
                             </div>
                             <div class="h-2 w-full bg-gray-100 dark:bg-gray-800 rounded-full overflow-hidden">
                                <div 
                                    class="h-full rounded-full transition-all duration-1000"
                                    :class="[
                                        'bg-gradient-to-r',
                                        idx === 0 ? 'from-orange-400 to-red-500' :
                                        idx === 1 ? 'from-blue-400 to-cyan-500' :
                                        idx === 2 ? 'from-purple-400 to-pink-500' :
                                        'from-gray-400 to-gray-500'
                                    ]"
                                    :style="{ width: `${(cat.articles_count / maxCategoryCount) * 100}%` }"
                                ></div>
                             </div>
                        </div>
                     </div>
                </div>
            </div>

            <!-- Newsletter -->
            <div class="bg-gradient-to-br from-indigo-900 to-slate-900 rounded-2xl p-8 text-center text-white relative overflow-hidden">
                <div class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20"></div>
                <div class="absolute -top-10 -right-10 w-40 h-40 bg-purple-500/30 rounded-full blur-3xl"></div>
                
                <div class="relative z-10">
                    <span class="material-symbols-outlined text-4xl mb-4 text-purple-400">mark_email_unread</span>
                    <h3 class="text-xl font-bold mb-2">订阅周刊</h3>
                    <p class="text-slate-300 text-sm mb-6 leading-relaxed">
                        不错过任何深度文章。我们承诺不发送垃圾邮件。
                    </p>
                    <div class="flex flex-col gap-3">
                        <input 
                            v-model="email" 
                            type="email" 
                            placeholder="您的邮箱地址" 
                            class="w-full bg-white/10 border border-white/20 rounded-lg px-4 py-2.5 text-sm text-white placeholder-white/40 focus:ring-2 focus:ring-purple-400 focus:border-transparent outline-none transition-all"
                        >
                        <button 
                            @click="openSubscribeModal(email)" 
                            class="w-full py-2.5 bg-white text-slate-900 rounded-lg text-sm font-bold hover:bg-purple-50 transition-colors shadow-lg"
                        >
                            订阅
                        </button>
                    </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import api from '@/api'

export default {
  name: 'Topics',
  inject: ['openSubscribeModal'],
  data() {
    return {
      categories: [],
      tags: [],
      loadingCategories: true,
      loadingTags: true,
      email: '',
      searchQuery: ''
    }
  },
  created() {
    this.fetchCategories()
    this.fetchTags()
  },
  computed: {
    sortedCategories() {
      // Create a copy and sort by article count descending
      return [...this.categories].sort((a, b) => (b.articles_count || 0) - (a.articles_count || 0))
    },
    maxCategoryCount() {
      if (!this.categories.length) return 0
      return Math.max(...this.categories.map(c => c.articles_count || 0))
    },
    filteredCategories() {
      if (!this.searchQuery) return this.categories
      const query = this.searchQuery.toLowerCase()
      return this.categories.filter(c => 
        c.name.toLowerCase().includes(query) || 
        (c.description && c.description.toLowerCase().includes(query))
      )
    },
    filteredTags() {
        if (!this.searchQuery) return this.tags
        const query = this.searchQuery.toLowerCase()
        return this.tags.filter(t => t.name.toLowerCase().includes(query))
    }
  },
  methods: {
    async fetchCategories() {
      try {
        const response = await api.getCategories()
        this.categories = response.data.results || response.data
      } catch (err) {
        console.error('Failed to fetch categories:', err)
      } finally {
        this.loadingCategories = false
      }
    },
    async fetchTags() {
      try {
        const response = await api.getTags()
        this.tags = response.data.results || response.data
      } catch (err) {
        console.error('Failed to fetch tags:', err)
      } finally {
        this.loadingTags = false
      }
    }
  }
}
</script>

<style scoped>
/* Add any view-specific styles here if Tailwind isn't enough */
</style>