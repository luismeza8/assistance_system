/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './members/templates/**/*.html',
    './registro/templates/**/base.html',
    './registro/templates/**/**/*.html',
    './registro/templates/**/**/*.html'
  ],
  theme: {
    extend: {
      colors: {
        primary: '#1E1D4F',
        secondary: '#E7E7FA'
      },
      fontFamily: {
        'montserrat': ['Montserrat']
      },
    },
  },
  plugins: [],
}

