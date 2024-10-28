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
      },

      keyframes: {
        spinningArrow: {
          "0%": {
            transform: "translateX(0px)",
          },
          "50%": {
            transform: "translateX(20px)",
          },
          "51%": {
            transform: "translateX(-20px)",
          },
          "100%": {
            transform: "translateX(0px)",
          }
        }
      },

      animation: {
        spinningArrow: "spinningArrow 0.3s ease-in-out 1",
      },
    },
  },
  plugins: [],
}

