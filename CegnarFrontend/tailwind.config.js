/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],

  theme: {
    extend: {
      colors: {
        textPrimary: "rgb(239, 231, 210);",
        textSecondary: "#c9c9c9",
        background: "#000000",
      },
      fontFamily: {
        heading: ["HeadingFont", "sans-serif"],
      }
    },
  },
  plugins: [],
}

