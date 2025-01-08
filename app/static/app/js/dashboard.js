// Receber dados do template
const income = parseFloat(document.getElementById('total-income').textContent);
const expense = parseFloat(document.getElementById('total-expense').textContent);

// Renderizar o gráfico de pizza
const ctx = document.getElementById('incomeExpenseChart').getContext('2d');
new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Receitas', 'Despesas'],
        datasets: [{
            data: [income, expense],
            backgroundColor: [
                'rgba(54, 162, 235, 0.7)',
                'rgba(255, 99, 132, 0.7)' 
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 99, 132, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        const value = tooltipItem.raw; // Valor bruto
                        const total = income + expense; // Soma total
                        const percentage = ((value / total) * 100).toFixed(2); // Porcentagem
                        return `${tooltipItem.label}: R$ ${value.toLocaleString()} (${percentage}%)`;
                    }
                }
            }
        }
    }
});
