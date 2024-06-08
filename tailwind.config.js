/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './members/templates/**/*.html',
    './registro/templates/registro/base.html'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1E1D4F',
        secondary: '#E7E7FA'
      }
    },
  },
  plugins: [],
}

