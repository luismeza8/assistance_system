document.addEventListener('DOMContentLoaded', function() {
  const value = JSON.parse(document.getElementById('hours').textContent);
  console.log(value)

  htmx.onLoad(function(){
    console.log('yeap')
  })
})
