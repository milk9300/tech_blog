<template>
  <div class="min-h-screen bg-white dark:bg-[#0f172a] relative">
    
    <!-- Reading Progress Bar -->
    <div class="fixed top-0 left-0 h-1 bg-gradient-to-r from-blue-400 to-purple-500 z-[60] transition-all duration-100 ease-out" :style="{ width: readingProgress + '%' }"></div>

    <!-- Loading State -->
    <div v-if="loading" class="max-w-[1200px] mx-auto px-6 py-20 animate-pulse">
        <div class="h-[400px] bg-gray-200 dark:bg-gray-800 rounded-3xl mb-12 w-full"></div>
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
            <div class="lg:col-span-8 space-y-8">
                <div class="h-10 bg-gray-200 dark:bg-gray-800 rounded-xl w-3/4 mb-6"></div>
                <div class="space-y-4">
                    <div class="h-4 bg-gray-200 dark:bg-gray-800 rounded w-full"></div>
                    <div class="h-4 bg-gray-200 dark:bg-gray-800 rounded w-full"></div>
                    <div class="h-4 bg-gray-200 dark:bg-gray-800 rounded w-5/6"></div>
                </div>
            </div>
            <div class="lg:col-span-4 hidden lg:block space-y-6">
                <div class="h-64 bg-gray-200 dark:bg-gray-800 rounded-2xl"></div>
            </div>
        </div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="min-h-[60vh] flex flex-col items-center justify-center text-center px-6">
         <div class="w-32 h-32 bg-gray-100 dark:bg-gray-800 rounded-full flex items-center justify-center text-gray-400 mb-6 relative overflow-hidden">
            <span class="material-symbols-outlined text-6xl relative z-10">sentiment_dissatisfied</span>
         </div>
         <h2 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">哎呀，加载失败了</h2>
         <p class="text-gray-500 dark:text-gray-400 mb-8 max-w-md">{{ error }}</p>
         <button @click="fetchArticle" class="px-8 py-3 bg-slate-900 dark:bg-white text-white dark:text-slate-900 rounded-xl font-bold hover:shadow-lg hover:-translate-y-0.5 transition-all duration-300">
            重新加载试试
         </button>
    </div>

    <div v-else-if="article">
        <!-- Immersive Hero Header -->
        <div class="relative w-full h-[50vh] min-h-[400px] bg-slate-900 dark:bg-[#0f172a] overflow-hidden flex items-end">
            <!-- Background Image/Gradient -->
            <div class="absolute inset-0 z-0">
                <img v-if="article.cover_image" :src="article.cover_image" class="w-full h-full object-cover opacity-60 dark:opacity-40" :alt="article.title">
                <div v-else class="w-full h-full bg-gradient-to-br from-slate-800 to-slate-900 opacity-90">
                     <div class="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20"></div>
                </div>
                <div class="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/60 to-transparent"></div>
            </div>

            <!-- Header Content -->
            <div class="relative z-10 max-w-[1200px] w-full mx-auto px-6 pb-12 md:pb-20">
                <!-- Breadcrumb -->
                <nav class="flex items-center gap-2 text-sm font-medium text-gray-300 mb-6 opacity-90 hover:opacity-100 transition-opacity">
                    <router-link to="/" class="hover:text-white transition-colors">首页</router-link>
                    <span class="material-symbols-outlined text-sm">chevron_right</span>
                    <router-link v-if="article.category" :to="{ name: 'CategoryList', params: { category: article.category.slug } }" class="hover:text-white transition-colors">
                        {{ article.category.name }}
                    </router-link>
                    <span v-else>文章</span>
                </nav>

                <h1 class="text-3xl md:text-5xl lg:text-6xl font-black text-white mb-6 leading-tight font-display tracking-tight drop-shadow-2xl">
                    {{ article.title }}
                </h1>

                <div class="flex flex-wrap items-center gap-6 text-sm md:text-base text-gray-200 font-medium">
                     <div class="flex items-center gap-2">
                        <span class="material-symbols-outlined text-lg text-blue-400">calendar_today</span>
                        <span>{{ formatDate(article.published_at) }}</span>
                     </div>
                     <div class="flex items-center gap-2">
                         <span class="material-symbols-outlined text-lg text-purple-400">visibility</span>
                         <span>{{ article.view_count }} 次阅读</span>
                     </div>
                     <div v-if="article.category" class="px-3 py-1 rounded-full bg-white/10 border border-white/20 text-white text-xs font-bold uppercase tracking-wider backdrop-blur-md">
                         {{ article.category.name }}
                     </div>
                </div>
            </div>
        </div>

        <!-- Main Layout (Grid) -->
        <div class="max-w-[1200px] mx-auto px-6 py-12 grid grid-cols-1 lg:grid-cols-12 gap-12">
            
            <!-- Left Column: Article Content (8 cols) -->
            <main class="lg:col-span-8">
                <!-- Markdown Body (Using the optimized typography) -->
                <article class="markdown-body" v-html="renderedContent"></article>

                <!-- Tags -->
                <div v-if="article.tags && article.tags.length" class="mt-16 pt-8 border-t border-gray-100 dark:border-gray-800">
                     <div class="flex flex-wrap gap-2">
                        <router-link 
                            v-for="tag in article.tags" 
                            :key="tag.id" 
                            :to="{ name: 'TagList', params: { tag: tag.slug } }"
                            class="px-4 py-1.5 rounded-full bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300 text-sm font-medium hover:bg-blue-500 hover:text-white dark:hover:bg-blue-600 transition-colors"
                        >
                            # {{ tag.name }}
                        </router-link>
                     </div>
                </div>

                <!-- Post Navigation -->
                <div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div class="p-6 rounded-2xl border border-gray-100 dark:border-gray-800 hover:border-blue-500/30 hover:bg-blue-50/30 dark:hover:bg-blue-900/10 transition-all group cursor-pointer bg-white dark:bg-transparent shadow-sm hover:shadow-md">
                        <div class="flex items-center gap-2 text-xs text-gray-400 mb-2 font-bold uppercase tracking-wider">
                            <span class="material-symbols-outlined text-sm">arrow_back</span>
                            上一篇
                        </div>
                        <div class="font-bold text-slate-700 dark:text-slate-300 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors line-clamp-1">
                            探索全栈开发的艺术
                        </div>
                    </div>
                    <div class="p-6 rounded-2xl border border-gray-100 dark:border-gray-800 hover:border-blue-500/30 hover:bg-blue-50/30 dark:hover:bg-blue-900/10 transition-all group cursor-pointer bg-white dark:bg-transparent shadow-sm hover:shadow-md text-right">
                        <div class="flex items-center justify-end gap-2 text-xs text-gray-400 mb-2 font-bold uppercase tracking-wider">
                            下一篇
                            <span class="material-symbols-outlined text-sm">arrow_forward</span>
                        </div>
                        <div class="font-bold text-slate-700 dark:text-slate-300 group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors line-clamp-1">
                            深入理解 Vue 3 响应式原理
                        </div>
                    </div>
                </div>
            </main>

            <!-- Right Column: Sidebar (4 cols) -->
            <aside class="lg:col-span-4 space-y-8 h-full">
                 <!-- Author Card (Not Sticky) -->
                <div class="bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 shadow-sm">
                    <div class="flex items-center gap-4 mb-6">
                         <div class="w-16 h-16 rounded-full bg-slate-100 dark:bg-slate-800 flex items-center justify-center text-3xl shadow-inner border border-gray-200 dark:border-gray-700">
                             🦕
                         </div>
                         <div>
                             <h3 class="font-bold text-slate-900 dark:text-white text-lg">Tech Blogger</h3>
                             <p class="text-xs font-bold text-blue-500 uppercase tracking-wide">Full Stack Dev</p>
                         </div>
                    </div>
                    <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed mb-6">
                        分享关于后端架构、前端工程化以及 DevOps 的实践经验。
                    </p>
                    
                    <div class="grid grid-cols-2 gap-3 mb-6">
                        <button class="flex items-center justify-center gap-2 py-2.5 bg-slate-900 dark:bg-white text-white dark:text-slate-900 rounded-xl text-sm font-bold hover:opacity-90 transition-opacity">
                            <span class="material-symbols-outlined text-lg">add</span> 关注
                        </button>
                        <button class="flex items-center justify-center gap-2 py-2.5 bg-gray-100 dark:bg-gray-700 text-gray-700 dark:text-gray-200 rounded-xl text-sm font-bold hover:bg-gray-200 dark:hover:bg-gray-600 transition-colors">
                            <span class="material-symbols-outlined text-lg">mail</span> 私信
                        </button>
                    </div>

                    <div class="pt-6 border-t border-gray-100 dark:border-gray-700">
                        <h4 class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4">分享文章</h4>
                        <div class="flex justify-between">
                            <button class="w-10 h-10 rounded-full bg-blue-50 text-blue-600 flex items-center justify-center hover:bg-blue-100 transition-colors">
                                <span class="text-sm font-bold">W</span>
                            </button>
                            <button class="w-10 h-10 rounded-full bg-sky-50 text-sky-600 flex items-center justify-center hover:bg-sky-100 transition-colors">
                                <span class="text-sm font-bold">T</span>
                            </button>
                            <button class="w-10 h-10 rounded-full bg-green-50 text-green-600 flex items-center justify-center hover:bg-green-100 transition-colors">
                                <span class="text-sm font-bold">W</span>
                            </button>
                            <button class="w-10 h-10 rounded-full bg-gray-50 text-gray-600 flex items-center justify-center hover:bg-gray-100 transition-colors">
                                <span class="material-symbols-outlined text-lg">link</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Table of Contents (Sticky) -->
                <!-- Only show when lg (desktop) and sticky at top-24 (below header) -->
                <div class="hidden lg:block sticky top-24">
                    <div class="bg-white dark:bg-[#1e293b] rounded-2xl p-6 border border-gray-100 dark:border-gray-800 shadow-sm">
                        <h3 class="font-bold text-slate-900 dark:text-white mb-4 flex items-center gap-2 pb-4 border-b border-gray-100 dark:border-gray-800">
                            <span class="material-symbols-outlined text-gray-400">format_list_bulleted</span> 
                            目录
                        </h3>
                        <nav v-if="toc.length > 0" class="max-h-[60vh] overflow-y-auto pr-2 scrollbar-thin">
                            <ul class="space-y-1 text-sm relative">
                                <div class="absolute left-0 top-0 bottom-0 w-0.5 bg-gray-100 dark:bg-gray-700"></div>
                                <li v-for="(item, idx) in toc" :key="idx" :style="{ paddingLeft: `${(item.level - 1) * 12}px` }" class="relative">
                                    <a 
                                        :href="`#${item.id}`" 
                                        class="block py-1.5 pl-3 border-l-2 transition-all duration-200 hover:text-blue-600 dark:hover:text-blue-400"
                                        :class="[
                                            activeId === item.id 
                                            ? 'border-blue-500 text-blue-600 dark:text-blue-400 font-bold bg-blue-50/50 dark:bg-blue-900/20 rounded-r-lg' 
                                            : 'border-transparent text-gray-500 dark:text-gray-400 hover:border-gray-300 dark:hover:border-gray-600'
                                        ]"
                                        @click.prevent="scrollToHeading(item.id)"
                                    >
                                        {{ item.text }}
                                    </a>
                                </li>
                            </ul>
                        </nav>
                        <div v-else class="text-sm text-gray-400 italic py-4 text-center">暂无目录</div>
                    </div>
                </div>
            </aside>
        </div>
    </div>

    <!-- Back to Top Button -->
    <button 
        @click="scrollToTop" 
        class="fixed bottom-8 right-8 p-3 bg-white dark:bg-slate-800 text-slate-900 dark:text-white border border-gray-200 dark:border-gray-700 rounded-full shadow-xl transition-all duration-300 z-40 hover:scale-110 active:scale-95 flex items-center justify-center group"
        :class="showBackToTop ? 'translate-y-0 opacity-100' : 'translate-y-16 opacity-0 pointer-events-none'"
    >
        <span class="material-symbols-outlined text-xl group-hover:-translate-y-0.5 transition-transform">arrow_upward</span>
    </button>
  </div>
</template>

<script>
import api from '@/api'
import moment from 'moment'
import { marked } from 'marked'
import hljs from 'highlight.js'
import 'highlight.js/styles/github-dark.css'

export default {
  name: 'ArticleDetail',
  data() {
    return {
      article: null,
      loading: true,
      error: null,
      readingProgress: 0,
      showBackToTop: false,
      toc: [],
      activeId: ''
    }
  },
  computed: {
    renderedContent() {
      if (!this.article || !this.article.content) return ''
      
      const renderer = new marked.Renderer()
      // Custom renderer to add IDs to headings for ToC
      // Using a regex that supports Chinese characters, English, numbers
      renderer.heading = (text, level) => {
        const slug = text.toLowerCase().replace(/[^\w\u4e00-\u9fa5]+/g, '-')
        return `<h${level} id="${slug}">${text}</h${level}>`
      }
      return marked.parse(this.article.content, { renderer })
    }
  },
  watch: {
    '$route.params.slug': 'fetchArticle'
  },
  created() {
    this.fetchArticle()
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll)
    // Cleanup observer
    if (this.observer) {
        this.observer.disconnect()
    }
  },
  methods: {
    async fetchArticle() {
      this.loading = true
      this.error = null
      const slug = this.$route.params.slug
      try {
        const response = await api.getArticle(slug)
        this.article = response.data
        this.$nextTick(() => {
            this.highlightCode()
            this.generateToC()
            this.setupObserver()
        })
      } catch (err) {
        this.error = '文章加载失败，请检查网络或稍后再试。'
        console.error(err)
      } finally {
        this.loading = false
      }
    },
    formatDate(date) {
      if (!date) return ''
      return moment(date).format('YYYY年MM月DD日')
    },
    highlightCode() {
      const blocks = this.$el.querySelectorAll('pre code')
      blocks.forEach((block) => {
        hljs.highlightElement(block)
      })
    },
    generateToC() {
        if (!this.article || !this.article.content) return
        
        const headings = []
        // Ensure we are selecting from the rendered markdown body
        const contentDiv = this.$el.querySelector('.markdown-body')
        if (contentDiv) {
            // Only grab h1, h2, h3 for the ToC to avoid clutter
            const elements = contentDiv.querySelectorAll('h1, h2, h3')
            elements.forEach(el => {
                if (el.id) {
                    headings.push({
                        id: el.id,
                        text: el.textContent,
                        level: parseInt(el.tagName.substring(1))
                    })
                }
            })
        }
        this.toc = headings
    },
    setupObserver() {
        if (this.observer) this.observer.disconnect()
        
        const options = {
            root: null,
            rootMargin: '-100px 0px -60% 0px',
            threshold: 0
        }
        
        this.observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    this.activeId = entry.target.id
                }
            })
        }, options)

        const contentDiv = this.$el.querySelector('.markdown-body')
        if (contentDiv) {
            const elements = contentDiv.querySelectorAll('h1, h2, h3')
            elements.forEach(el => this.observer.observe(el))
        }
    },
    scrollToHeading(id) {
        const el = document.getElementById(id)
        if (el) {
            const offset = 100 
            const bodyRect = document.body.getBoundingClientRect().top
            const elementRect = el.getBoundingClientRect().top
            const elementPosition = elementRect - bodyRect
            const offsetPosition = elementPosition - offset

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            })
            // Manually set activeId to give immediate feedback
            this.activeId = id
        }
    },
    scrollToTop() {
        window.scrollTo({ top: 0, behavior: 'smooth' })
    },
    handleScroll() {
        this.showBackToTop = window.scrollY > 500
        const totalHeight = document.documentElement.scrollHeight - window.innerHeight
        const progress = (window.scrollY / totalHeight) * 100
        this.readingProgress = Math.min(100, Math.max(0, progress))
    }
  }
}
</script>

<style>
/* Typography System for Article Content 
  Based on the "optimized" version you liked
*/

.markdown-body {
    @apply text-slate-800 dark:text-slate-200;
    font-family: 'Noto Sans', sans-serif;
    font-size: 1.125rem; /* 18px text */
    line-height: 1.8;    /* Relaxed line height */
}

/* Paragraphs */
.markdown-body p {
    margin-bottom: 1.75em;
    letter-spacing: 0.01em;
}

/* Headings */
.markdown-body h1, 
.markdown-body h2, 
.markdown-body h3, 
.markdown-body h4 {
    @apply font-display font-bold text-slate-900 dark:text-white;
    margin-top: 2.5em;
    margin-bottom: 1em;
    line-height: 1.3;
    scroll-margin-top: 120px; /* Crucial for sticky header anchor linking */
}

.markdown-body h1 { font-size: 2.25em; }
.markdown-body h2 { 
    font-size: 1.75em; 
    border-bottom: 1px solid #e5e7eb; 
    padding-bottom: 0.3em;
    margin-top: 2em;
}
.dark .markdown-body h2 { border-color: #1f2937; }
.markdown-body h3 { font-size: 1.5em; }
.markdown-body h4 { font-size: 1.25em; }

/* Lists */
.markdown-body ul {
    list-style-type: disc;
    padding-left: 1.625em;
    margin-bottom: 1.75em;
}
.markdown-body ol {
    list-style-type: decimal;
    padding-left: 1.625em;
    margin-bottom: 1.75em;
}
.markdown-body li {
    margin-bottom: 0.5em;
    padding-left: 0.375em;
}
.markdown-body li::marker {
    @apply text-gray-400;
}

/* Links */
.markdown-body a {
    @apply text-blue-600 dark:text-blue-400 font-medium;
    text-decoration: underline;
    text-decoration-thickness: 1px;
    text-underline-offset: 2px;
    transition: color 0.2s;
}
.markdown-body a:hover {
    @apply text-blue-800 dark:text-blue-300;
}

/* Blockquotes */
.markdown-body blockquote {
    font-style: italic;
    border-left: 4px solid #e5e7eb;
    background-color: #f9fafb;
    padding: 1em 1.5em;
    margin-bottom: 2em;
    border-radius: 0.5rem;
    @apply text-gray-700 dark:text-gray-300 border-l-4 border-blue-500 bg-blue-50/50 dark:bg-slate-800/50 dark:border-blue-500/50;
}
.markdown-body blockquote p:last-child {
    margin-bottom: 0;
}

/* Code Blocks */
.markdown-body pre {
    background-color: #1e293b !important;
    color: #e2e8f0;
    border-radius: 0.75rem;
    padding: 1.25rem;
    overflow-x: auto;
    margin-top: 1.5em;
    margin-bottom: 2em;
    font-size: 0.875em;
    line-height: 1.7;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.markdown-body code {
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

/* Inline Code */
.markdown-body :not(pre) > code {
    @apply bg-gray-100 dark:bg-gray-800 text-pink-500 dark:text-pink-400;
    padding: 0.2em 0.4em;
    border-radius: 0.25rem;
    font-size: 0.875em;
    font-weight: 500;
}

/* Images */
.markdown-body img {
    border-radius: 0.75rem;
    margin-top: 2em;
    margin-bottom: 2em;
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    max-width: 100%;
}

/* Tables */
.markdown-body table {
    width: 100%;
    table-layout: auto;
    text-align: left;
    margin-top: 2em;
    margin-bottom: 2em;
    border-collapse: collapse;
}
.markdown-body thead {
    border-bottom: 1px solid #e5e7eb;
}
.dark .markdown-body thead { border-color: #374151; }
.markdown-body th {
    font-weight: 600;
    padding: 0.75em;
    vertical-align: bottom;
}
.markdown-body td {
    padding: 0.75em;
    border-bottom: 1px solid #f3f4f6;
    vertical-align: top;
}
.dark .markdown-body td { border-color: #1f2937; }

/* Smooth scroll & Scrollbar */
html {
    scroll-behavior: smooth;
}
.scrollbar-thin::-webkit-scrollbar {
  width: 4px;
}
.scrollbar-thin::-webkit-scrollbar-track {
  background: transparent;
}
.scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: #cbd5e1;
  border-radius: 20px;
}
.dark .scrollbar-thin::-webkit-scrollbar-thumb {
  background-color: #475569;
}
</style>