/**
 * EasyMDE Markdown Editor Initialization for Django Admin
 * Targets the 'content' textarea field on Article edit pages.
 */
(function () {
    'use strict';

    function initEasyMDE() {
        var contentTextarea = document.getElementById('id_content');

        if (!contentTextarea) {
            return;
        }

        // Check if EasyMDE is loaded
        if (typeof EasyMDE === 'undefined') {
            console.warn('EasyMDE not loaded, retrying in 500ms...');
            setTimeout(initEasyMDE, 500);
            return;
        }

        // Avoid re-initialization
        if (contentTextarea.dataset.easymdeInitialized) {
            return;
        }

        var easyMDE = new EasyMDE({
            element: contentTextarea,
            spellChecker: false,
            autosave: {
                enabled: true,
                uniqueId: 'article_content_' + (window.location.pathname.split('/').filter(Boolean).pop() || 'new'),
                delay: 5000,
            },
            toolbar: [
                'bold', 'italic', 'heading', '|',
                'quote', 'unordered-list', 'ordered-list', '|',
                'link', 'image', 'code', '|',
                'preview', 'side-by-side', 'fullscreen', '|',
                'guide'
            ],
            placeholder: '使用 Markdown 格式书写您的文章内容...',
            status: ['autosave', 'lines', 'words', 'cursor'],
            renderingConfig: {
                codeSyntaxHighlighting: true,
            },
            minHeight: '400px',
        });

        contentTextarea.dataset.easymdeInitialized = 'true';
        console.log('EasyMDE initialized for article content field.');
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initEasyMDE);
    } else {
        // DOM already loaded, check if EasyMDE script is ready
        setTimeout(initEasyMDE, 100);
    }
})();
