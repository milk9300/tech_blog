<template>
  <div class="min-h-screen">
    <!-- Hero Section -->
    <div class="relative overflow-hidden bg-white dark:bg-surface-dark border-b border-gray-100 dark:border-gray-800">
      <div class="absolute inset-0 bg-grid-slate-100 [mask-image:linear-gradient(0deg,white,rgba(255,255,255,0.6))] dark:bg-grid-slate-700/25 dark:[mask-image:linear-gradient(0deg,rgba(255,255,255,0.1),rgba(255,255,255,0.5))]"></div>
      <div class="max-w-[1000px] mx-auto px-6 py-24 relative z-10 text-center">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 text-primary text-xs font-bold uppercase tracking-wider mb-6">
          <span class="w-2 h-2 rounded-full bg-primary"></span>
          About The Project
        </div>
        <h1 class="text-5xl md:text-7xl font-black tracking-tight text-slate-900 dark:text-white mb-8 font-display">
          代码不止是逻辑 <br/>
          <span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-blue-400">更是表达的艺术</span>
        </h1>
        <p class="text-xl text-gray-500 dark:text-gray-400 max-w-2xl mx-auto leading-relaxed">
          书淮BLOG 不仅仅是一个技术博客，它是一个全栈开发的实验场，也是记录技术成长的数字花园。
        </p>
      </div>
    </div>

    <div class="max-w-[1000px] mx-auto px-6 py-16 space-y-24">
      <!-- Our Story -->
      <section class="grid md:grid-cols-2 gap-12 items-center">
        <div class="space-y-6">
          <h2 class="text-3xl font-bold text-slate-900 dark:text-white font-display">初心与愿景</h2>
          <div class="space-y-4 text-lg text-gray-600 dark:text-gray-300 leading-relaxed">
            <p>
              在这个信息爆炸的时代，找到高质量、系统性的技术内容变得越来越难。
            </p>
            <p>
              构建这个博客系统的初衷，是为了提供一个<b>纯粹</b>的阅读环境。这里没有复杂的算法推荐，只有经过深思熟虑的技术文章。同时也作为一个开源项目，展示现代 Web 开发的最佳实践。
            </p>
            <p>
              无论你是刚入门的开发者，还是寻求架构灵感的资深工程师，希望这里都能给你带来一些启发。
            </p>
          </div>
          
          <!-- Stats -->
          <div class="grid grid-cols-3 gap-6 pt-6 border-t border-gray-100 dark:border-gray-800">
            <div>
              <div class="text-3xl font-black text-slate-900 dark:text-white">100+</div>
              <div class="text-xs text-gray-500 uppercase font-bold mt-1">技术文章</div>
            </div>
            <div>
              <div class="text-3xl font-black text-slate-900 dark:text-white">2024</div>
              <div class="text-xs text-gray-500 uppercase font-bold mt-1">建立年份</div>
            </div>
            <div>
              <div class="text-3xl font-black text-slate-900 dark:text-white">Open</div>
              <div class="text-xs text-gray-500 uppercase font-bold mt-1">开源精神</div>
            </div>
          </div>
        </div>
        <div class="relative">
          <div class="absolute inset-0 bg-gradient-to-tr from-primary/20 to-purple-500/20 rounded-3xl transform rotate-3 blur-2xl"></div>
          <div class="relative bg-white dark:bg-[#1c2333] border border-gray-100 dark:border-gray-800 rounded-2xl p-8 shadow-xl">
             <div class="flex items-center gap-4 mb-6">
                <div class="size-16 rounded-full bg-gray-100 dark:bg-gray-800 flex items-center justify-center overflow-hidden">
                    <span class="material-symbols-outlined text-4xl text-gray-400">person</span>
                </div>
                <div>
                    <h3 class="text-xl font-bold text-slate-900 dark:text-white">Maintainer</h3>
                    <p class="text-primary font-medium">Full Stack Developer</p>
                </div>
             </div>
             <p class="text-gray-600 dark:text-gray-300 italic">
               "我相信好的代码应该像散文一样易读。在这个项目中，我试图在 Django 的稳健与 Vue 的灵动之间寻找完美的平衡。"
             </p>
             <div class="mt-6 flex gap-3">
                <a href="#" class="flex items-center gap-2 px-4 py-2 bg-slate-900 text-white rounded-lg text-sm font-bold hover:bg-slate-800 transition-colors">
                    <span class="material-symbols-outlined text-lg">code</span> GitHub
                </a>
                 <a href="#" class="flex items-center gap-2 px-4 py-2 bg-blue-500 text-white rounded-lg text-sm font-bold hover:bg-blue-600 transition-colors">
                    <span class="material-symbols-outlined text-lg">alternate_email</span> 联系我
                </a>
             </div>
          </div>
        </div>
      </section>

      <!-- Tech Stack -->
      <section>
        <div class="text-center mb-12">
           <h2 class="text-3xl font-bold text-slate-900 dark:text-white font-display mb-4">技术栈</h2>
           <p class="text-gray-500 dark:text-gray-400">本项目采用现代化的前后端分离架构构建，追求高性能与可维护性。</p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <!-- Backend -->
            <div class="p-6 rounded-2xl bg-gray-50 dark:bg-[#1c2333]/50 border border-gray-100 dark:border-gray-800 hover:border-primary/50 transition-colors group">
                <div class="w-12 h-12 rounded-xl bg-green-500/10 text-green-600 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                    <span class="material-symbols-outlined text-2xl">dns</span>
                </div>
                <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2">Backend Core</h3>
                <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">稳健的数据处理与 API 服务。</p>
                <ul class="space-y-2">
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-green-500"></span> Django 5.0
                    </li>
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-green-500"></span> Django REST Framework
                    </li>
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-green-500"></span> MySQL 8.0
                    </li>
                </ul>
            </div>

            <!-- Frontend -->
            <div class="p-6 rounded-2xl bg-gray-50 dark:bg-[#1c2333]/50 border border-gray-100 dark:border-gray-800 hover:border-primary/50 transition-colors group">
                <div class="w-12 h-12 rounded-xl bg-blue-500/10 text-blue-600 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                    <span class="material-symbols-outlined text-2xl">web</span>
                </div>
                <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2">Frontend Interactive</h3>
                <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">流畅的用户体验与响应式设计。</p>
                <ul class="space-y-2">
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span> Vue.js 2
                    </li>
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span> Tailwind CSS
                    </li>
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span> Vite
                    </li>
                </ul>
            </div>

            <!-- DevOps -->
            <div class="p-6 rounded-2xl bg-gray-50 dark:bg-[#1c2333]/50 border border-gray-100 dark:border-gray-800 hover:border-primary/50 transition-colors group">
                 <div class="w-12 h-12 rounded-xl bg-purple-500/10 text-purple-600 flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
                    <span class="material-symbols-outlined text-2xl">rocket_launch</span>
                </div>
                <h3 class="text-lg font-bold text-slate-900 dark:text-white mb-2">DevOps & Deploy</h3>
                <p class="text-sm text-gray-500 dark:text-gray-400 mb-4">自动化构建与容器化部署。</p>
                <ul class="space-y-2">
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span> Docker & Compose
                    </li>
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span> Nginx
                    </li>
                    <li class="flex items-center gap-2 text-sm text-slate-700 dark:text-gray-300">
                        <span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span> CI/CD Pipeline
                    </li>
                </ul>
            </div>
        </div>
      </section>

      <!-- Connect -->
      <section class="bg-slate-900 rounded-3xl p-12 text-center relative overflow-hidden">
        <div class="absolute top-0 right-0 w-64 h-64 bg-primary/20 rounded-full blur-3xl -mr-16 -mt-16"></div>
        <div class="absolute bottom-0 left-0 w-64 h-64 bg-blue-500/20 rounded-full blur-3xl -ml-16 -mb-16"></div>
        
        <div class="relative z-10">
          <h2 class="text-3xl font-bold text-white font-display mb-6">准备好开始交流了吗？</h2>
          <p class="text-slate-300 max-w-xl mx-auto mb-8">
            如果您有任何技术问题，或者想讨论合作机会，欢迎随时联系。
          </p>
          <div class="flex justify-center gap-4">
            <button class="px-8 py-3 bg-white text-slate-900 rounded-xl font-bold hover:bg-gray-100 transition-colors">
              订阅邮件
            </button>
            <button class="px-8 py-3 bg-transparent border border-white/20 text-white rounded-xl font-bold hover:bg-white/10 transition-colors">
              关于作者
            </button>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script lang="js">
export default {
    name: 'About'
}
</script>

<style scoped>
/* Optional: specific background grid pattern if not available in tailwind config */
.bg-grid-slate-100 {
  background-size: 40px 40px;
  background-image: linear-gradient(to right, #f1f5f9 1px, transparent 1px),
    linear-gradient(to bottom, #f1f5f9 1px, transparent 1px);
}
.dark .bg-grid-slate-700\/25 {
  background-size: 40px 40px;
  background-image: linear-gradient(to right, rgba(51, 65, 85, 0.25) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(51, 65, 85, 0.25) 1px, transparent 1px);
}
</style>