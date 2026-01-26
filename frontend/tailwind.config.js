/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#195de6",
                "background-light": "#FBFBFC",
                "background-dark": "#111621",
                "surface-light": "#FFFFFF",
                "surface-dark": "#1e2433",
            },
            fontFamily: {
                "display": ["Space Grotesk", "sans-serif"],
                "body": ["Noto Sans", "sans-serif"],
                "inter": ["Inter", "sans-serif"]
            },
        },
    },
    plugins: [],
}
