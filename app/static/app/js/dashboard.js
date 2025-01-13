// Income and Expense Ratio Chart
const income = parseFloat(document.getElementById('total-income').textContent);
const expense = parseFloat(document.getElementById('total-expense').textContent);

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
                    label: function (tooltipItem) {
                        const value = tooltipItem.raw;
                        const total = income + expense;
                        const percentage = ((value / total) * 100).toFixed(2);
                        return `${tooltipItem.label}: R$ ${value.toLocaleString()} (${percentage}%)`;
                    }
                }
            }
        }
    }
});

// Monthly Expense Chart
const months = document.getElementById('months-data').textContent;
const months_json = JSON.parse(months.slice(56));
const totals = document.getElementById('totals-data').textContent;
const totals_json = JSON.parse(totals.slice(56));

const ctxMonthly = document.getElementById('monthlyExpenseChart').getContext('2d');
new Chart(ctxMonthly, {
    type: 'line', 
    data: {
        labels: months_json,
        datasets: [{
            label: 'Gastos Mensais (R$)',
            data: totals_json,
            backgroundColor: 'rgba(255, 99, 132, 0.7)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Valor (R$)'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Meses'
                }
            }
        },
        plugins: {
            legend: {
                display: false
            }
        }
    }
});