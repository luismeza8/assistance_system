/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './members/templates/**/*.html',
    './registro/templates/registro/base.html',
    './registro/templates/registro/miembros/miembros.html'
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

