  (() => {
    const ctx = document.getElementById('register_chart');
    const value = JSON.parse(document.getElementById('hours').textContent);

    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
        datasets: [{
          label: 'Horas trabajadas cada dia',
          backgroundColor: '#1e1d4f',
          data: value,
        }]
      },
      options: {
        aspectRatio: 5,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })();
