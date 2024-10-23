/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {
      colors: {
        background: "#000000",
      },
      fontFamily: {
        heading: ["HeadingFont", "sans-serif"],
      }
    },
  },
  plugins: [],
}

