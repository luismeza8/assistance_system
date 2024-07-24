  (() => {
    const chartConfig = document.getElementById('register_chart');
    const hoursWorked = JSON.parse(document.getElementById('hours').textContent);

    new Chart(chartConfig, {
      type: 'bar',
      data: {
        labels: ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo'],
        datasets: [{
          label: 'Horas trabajadas cada dia',
          backgroundColor: '#1e1d4f',
          data: hoursWorked,
        }]
      },
      options: {
        aspectRatio: 3,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  })();
