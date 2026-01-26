<template>
  <div class="min-h-screen">
    <div class="flex flex-col min-h-screen bg-background-light dark:bg-[#0f172a] text-slate-900 dark:text-slate-100 transition-colors duration-300">
      
      <!-- Top Navigation Bar -->
      <header class="sticky top-0 z-50 w-full border-b border-gray-200 dark:border-gray-800 bg-white/80 dark:bg-[#0f172a]/80 backdrop-blur-xl transition-all duration-300">
        <div class="max-w-[1200px] mx-auto px-6 h-16 flex items-center justify-between">
          
          <!-- Logo & Desktop Nav -->
          <div class="flex items-center gap-10">
            <router-link to="/" class="flex items-center gap-2 group">
              <div class="size-8 bg-gradient-to-tr from-blue-600 to-purple-600 rounded-lg flex items-center justify-center text-white shadow-lg shadow-blue-500/20 group-hover:scale-110 transition-transform duration-300">
                <span class="material-symbols-outlined text-xl">terminal</span>
              </div>
              <h1 class="text-xl font-bold tracking-tight text-slate-900 dark:text-white font-display group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">书淮BLOG</h1>
            </router-link>
            
            <nav class="hidden md:flex items-center gap-1 p-1 bg-gray-100/50 dark:bg-gray-800/50 rounded-full border border-gray-200/50 dark:border-gray-700/50 backdrop-blur-sm">
              <router-link 
                v-for="link in navLinks" 
                :key="link.path" 
                :to="link.path"
                class="px-4 py-1.5 text-sm font-bold rounded-full transition-all duration-300 relative"
                active-class="bg-white dark:bg-slate-700 text-blue-600 dark:text-blue-400 shadow-sm"
                :class="[$route.path !== link.path ? 'text-gray-500 dark:text-gray-400 hover:text-slate-900 dark:hover:text-white' : '']"
              >
                {{ link.name }}
              </router-link>
            </nav>
          </div>

          <!-- Right Actions -->
          <div class="flex items-center gap-2 md:gap-4">
            <!-- Search Bar (Desktop) -->
            <div class="relative hidden md:flex items-center group">
               <div :class="['absolute right-0 flex items-center transition-all duration-300 overflow-hidden bg-gray-100 dark:bg-gray-800 rounded-full', showSearch ? 'w-64 px-4 py-1.5 border border-blue-500/30 ring-2 ring-blue-500/10' : 'w-10 h-10 bg-transparent dark:bg-transparent']">
                  <input
                    ref="searchInput"
                    v-model="searchQuery"
                    @keyup.enter="handleSearch"
                    type="text"
                    placeholder="搜索文章..."
                    class="w-full bg-transparent border-none text-sm focus:ring-0 outline-none placeholder-gray-400"
                    :class="{ 'opacity-0': !showSearch }"
                  />
               </div>
               <button 
                  @click="toggleSearch"
                  class="relative z-10 w-10 h-10 flex items-center justify-center rounded-full text-gray-500 hover:text-blue-600 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
               >
                  <span class="material-symbols-outlined">{{ showSearch ? 'search' : 'search' }}</span>
               </button>
            </div>

            <!-- Theme Toggle -->
            <button
              @click="toggleDarkMode"
              class="w-10 h-10 flex items-center justify-center rounded-full text-gray-500 hover:text-orange-500 hover:bg-orange-50 dark:hover:text-yellow-400 dark:hover:bg-yellow-400/10 transition-colors focus:outline-none"
            >
              <span class="material-symbols-outlined transform transition-transform duration-500 rotate-0 dark:rotate-180">
                {{ isDarkMode ? 'light_mode' : 'dark_mode' }}
              </span>
            </button>
            
            <!-- Subscribe Button (Desktop) -->
            <button 
              @click="showSubscribeModal = true"
              class="hidden md:flex bg-slate-900 dark:bg-white hover:bg-slate-800 dark:hover:bg-gray-200 text-white dark:text-slate-900 text-sm font-bold px-5 py-2.5 rounded-xl transition-all shadow-lg shadow-slate-900/20 dark:shadow-none hover:-translate-y-0.5"
            >
              订阅
            </button>

            <!-- Mobile Menu Toggle -->
            <button 
                @click="mobileMenuOpen = !mobileMenuOpen"
                class="md:hidden w-10 h-10 flex items-center justify-center rounded-full text-gray-500 hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors"
            >
                <span class="material-symbols-outlined">{{ mobileMenuOpen ? 'close' : 'menu' }}</span>
            </button>
          </div>
        </div>

        <!-- Mobile Menu Dropdown -->
        <transition name="slide-fade">
          <div 
              v-if="mobileMenuOpen"
              class="md:hidden absolute top-16 left-0 w-full bg-white dark:bg-[#0f172a] border-b border-gray-200 dark:border-gray-800 p-6 shadow-2xl origin-top"
          >
              <nav class="flex flex-col gap-4">
                  <router-link 
                      v-for="link in navLinks" 
                      :key="link.path" 
                      :to="link.path"
                      @click.native="mobileMenuOpen = false"
                      class="text-lg font-bold p-2 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-800 transition-colors"
                      :class="[$route.path === link.path ? 'text-blue-600 dark:text-blue-400' : 'text-gray-600 dark:text-gray-300']"
                  >
                      {{ link.name }}
                  </router-link>
                  <div class="h-px bg-gray-100 dark:bg-gray-800 my-2"></div>
                  
                  <!-- Mobile Search -->
                  <div class="relative">
                      <span class="absolute left-3 top-1/2 -translate-y-1/2 material-symbols-outlined text-gray-400">search</span>
                      <input 
                          v-model="searchQuery"
                          @keyup.enter="handleSearch"
                          type="text" 
                          placeholder="搜索..." 
                          class="w-full bg-gray-100 dark:bg-gray-800 rounded-xl py-3 pl-10 pr-4 outline-none focus:ring-2 focus:ring-blue-500"
                      >
                  </div>

                  <button 
                    @click="showSubscribeModal = true; mobileMenuOpen = false"
                    class="w-full bg-blue-600 text-white font-bold py-3 rounded-xl shadow-lg shadow-blue-600/20"
                  >
                    订阅更新
                  </button>
              </nav>
          </div>
        </transition>
      </header>

      <!-- Subscribe Modal -->
      <transition
        enter-active-class="transition ease-out duration-300"
        enter-from-class="opacity-0 scale-95"
        enter-to-class="opacity-100 scale-100"
        leave-active-class="transition ease-in duration-200"
        leave-from-class="opacity-100 scale-100"
        leave-to-class="opacity-0 scale-95"
      >
        <div v-if="showSubscribeModal" class="fixed inset-0 z-[100] flex items-center justify-center p-6">
            <div class="absolute inset-0 bg-slate-900/60 backdrop-blur-sm" @click="showSubscribeModal = false"></div>
            <div class="relative bg-white dark:bg-[#1e293b] w-full max-w-md rounded-3xl p-8 shadow-2xl border border-gray-100 dark:border-gray-700">
            <div class="text-center mb-8">
                <div class="w-16 h-16 bg-blue-50 dark:bg-blue-900/20 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-4">
                    <span class="material-symbols-outlined text-3xl">mail</span>
                </div>
                <h3 class="text-2xl font-bold text-slate-900 dark:text-white mb-2 font-display">订阅我们的通讯</h3>
                <p class="text-gray-500 dark:text-gray-400 text-sm">获取关于 Web 开发和技术趋势的最新更新，绝无垃圾邮件。</p>
            </div>
            
            <form @submit.prevent="handleSubscribe" class="space-y-4">
                <div>
                <input 
                    v-model="subscriberEmail"
                    type="email" 
                    required
                    placeholder="you@example.com"
                    class="w-full px-4 py-3 rounded-xl bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:bg-white dark:focus:bg-gray-800 transition-all text-slate-900 dark:text-white placeholder-gray-400"
                />
                </div>
                <button 
                type="submit"
                :disabled="submitting"
                class="w-full py-3.5 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 disabled:opacity-50 disabled:cursor-not-allowed text-white font-bold rounded-xl transition-all shadow-lg shadow-blue-500/25 transform active:scale-95"
                >
                <div v-if="submitting" class="flex items-center justify-center gap-2">
                    <span class="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
                    <span>处理中...</span>
                </div>
                <span v-else>立即订阅</span>
                </button>
            </form>

            <div v-if="subscribeMessage" class="mt-4 p-3 rounded-lg text-center text-sm font-medium animate-in fade-in slide-in-from-bottom-2" :class="[subscribeSuccess ? 'bg-green-50 text-green-600 dark:bg-green-900/20 dark:text-green-400' : 'bg-red-50 text-red-600 dark:bg-red-900/20 dark:text-red-400']">
                {{ subscribeMessage }}
            </div>

            <button @click="showSubscribeModal = false" class="absolute top-4 right-4 p-2 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200 transition-colors rounded-full hover:bg-gray-100 dark:hover:bg-gray-800">
                <span class="material-symbols-outlined">close</span>
            </button>
            </div>
        </div>
      </transition>

      <!-- Main Content -->
      <main class="flex-grow">
         <!-- Fix: Use Vue 2 Router syntax -->
         <transition name="fade" mode="out-in">
            <router-view></router-view>
         </transition>
      </main>

      <!-- Footer -->
      <footer class="bg-white dark:bg-[#0d1117] border-t border-gray-200 dark:border-gray-800 py-16 mt-20">
        <div class="max-w-[1200px] mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-12">
          <div class="col-span-1 md:col-span-2 space-y-6">
            <div class="flex items-center gap-3 text-slate-900 dark:text-white">
              <div class="size-8 bg-blue-600 rounded-lg flex items-center justify-center text-white">
                <span class="material-symbols-outlined text-xl">terminal</span>
              </div>
              <h2 class="text-xl font-bold font-display">书淮BLOG</h2>
            </div>
            <p class="text-gray-500 dark:text-[#9da6b8] text-sm leading-relaxed max-w-sm">
              深入探讨现代 Web 开发、软件工程模式和技术未来的文章和教程。专为专业开发者策划。
            </p>
            <div class="flex gap-4">
                <a href="#" class="w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-500 hover:bg-blue-600 hover:text-white transition-all duration-300">
                    <span class="text-sm font-bold">𝕏</span>
                </a>
                <a href="#" class="w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-500 hover:bg-gray-900 hover:text-white transition-all duration-300">
                     <span class="text-sm font-bold">Gh</span>
                </a>
                <a href="#" class="w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center text-gray-500 hover:bg-blue-700 hover:text-white transition-all duration-300">
                     <span class="text-sm font-bold">in</span>
                </a>
            </div>
          </div>
          <div>
            <h6 class="text-slate-900 dark:text-white font-bold mb-6 font-display">探索</h6>
            <ul class="flex flex-col gap-3 text-gray-500 dark:text-[#9da6b8] text-sm">
              <li><router-link to="/" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors flex items-center gap-2"><span class="w-1 h-1 bg-gray-300 rounded-full"></span>所有文章</router-link></li>
              <li><router-link to="/topics" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors flex items-center gap-2"><span class="w-1 h-1 bg-gray-300 rounded-full"></span>话题分类</router-link></li>
              <li><router-link to="/about" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors flex items-center gap-2"><span class="w-1 h-1 bg-gray-300 rounded-full"></span>关于我们</router-link></li>
            </ul>
          </div>
          <div>
            <h6 class="text-slate-900 dark:text-white font-bold mb-6 font-display">资源</h6>
            <ul class="flex flex-col gap-3 text-gray-500 dark:text-[#9da6b8] text-sm">
              <li><a href="#" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">RSS 订阅</a></li>
              <li><a href="#" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">开源贡献</a></li>
              <li><a href="#" class="hover:text-blue-600 dark:hover:text-blue-400 transition-colors">友情链接</a></li>
            </ul>
          </div>
        </div>
        <div class="max-w-[1200px] mx-auto px-6 mt-16 pt-8 border-t border-gray-200 dark:border-gray-800 flex flex-col md:flex-row justify-between items-center gap-4">
          <p class="text-gray-400 dark:text-gray-600 text-xs">© 2024 书淮BLOG. Designed & Built with ❤️.</p>
          <div class="flex gap-6 text-gray-400 dark:text-gray-600 text-xs font-medium">
            <a href="#" class="hover:text-slate-900 dark:hover:text-white transition-colors">隐私政策</a>
            <a href="#" class="hover:text-slate-900 dark:hover:text-white transition-colors">服务条款</a>
            <a href="#" class="hover:text-slate-900 dark:hover:text-white transition-colors">Sitemap</a>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script>
import api from '@/api'

export default {
  name: 'App',
  data() {
    return {
      isDarkMode: false,
      showSearch: false,
      searchQuery: '',
      showSubscribeModal: false,
      mobileMenuOpen: false,
      subscriberEmail: '',
      submitting: false,
      subscribeMessage: '',
      subscribeSuccess: false,
      navLinks: [
        { name: '首页', path: '/' },
        { name: '话题', path: '/topics' },
        { name: '关于', path: '/about' }
      ]
    }
  },
  provide() {
    return {
      openSubscribeModal: this.openSubscribeModal
    }
  },
  watch: {
    '$route'() {
        this.mobileMenuOpen = false
        this.showSearch = false
        window.scrollTo(0, 0)
    }
  },
  methods: {
    openSubscribeModal(email) {
      if (typeof email === 'string') {
        this.subscriberEmail = email
      }
      this.showSubscribeModal = true
    },
    toggleDarkMode() {
      this.isDarkMode = !this.isDarkMode;
      if (this.isDarkMode) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
      }
    },
    toggleSearch() {
      this.showSearch = !this.showSearch
      if (this.showSearch) {
        this.$nextTick(() => {
            this.$refs.searchInput.focus()
        })
      } else {
        this.searchQuery = ''
      }
    },
    handleSearch() {
      if (!this.searchQuery.trim()) return
      this.$router.push({ path: '/', query: { search: this.searchQuery } })
      // Don't close immediately on desktop to allow continuous search, or close if you prefer
      if (window.innerWidth < 768) {
         this.mobileMenuOpen = false
      }
      this.showSearch = false
      this.searchQuery = ''
    },
    async handleSubscribe() {
      if (!this.subscriberEmail) return
      this.submitting = true
      this.subscribeMessage = ''
      try {
        await api.subscribe(this.subscriberEmail)
        this.subscribeSuccess = true
        this.subscribeMessage = '感谢订阅！我们很快会联系您。'
        this.subscriberEmail = ''
        setTimeout(() => {
          this.showSubscribeModal = false
          this.subscribeMessage = ''
        }, 3000)
      } catch (err) {
        this.subscribeSuccess = false
        this.subscribeMessage = err.response?.data?.email?.[0] || '订阅失败，请稍后重试。'
      } finally {
        this.submitting = false
      }
    }
  },
  created() {
    // Check local storage or media preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        this.isDarkMode = savedTheme === 'dark';
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
        this.isDarkMode = true;
    }
    
    if (this.isDarkMode) {
        document.documentElement.classList.add('dark');
    }
  }
}
</script>

<style>
/* Page Transition Animation */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Slide Fade Animation for Mobile Menu */
.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.3s ease;
}
.slide-fade-enter,
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>