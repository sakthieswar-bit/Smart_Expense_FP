/* DELETE CONFIRMATION */
function confirmDelete() {
    return confirm("Are you sure you want to delete this item?");
}

/* DATE INPUT DEFAULT + CHARTS */
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('input[type="date"]').forEach(function (input) {
        if (!input.value) {
            input.value = new Date().toISOString().split("T")[0];
        }
    });
    initializeDashboardCharts();
});

/* DASHBOARD CHARTS */
function initializeDashboardCharts() {
    if (typeof Chart === "undefined") return;

    const expenseCanvas = document.getElementById("expenseCategoryChart");
    const incomeExpenseCanvas = document.getElementById("incomeExpenseChart");
    if (!expenseCanvas && !incomeExpenseCanvas) return;

    const dashboardData = document.getElementById("dashboardChartData");
    if (!dashboardData) return;

    let categoryLabels = [];
    let categoryValues = [];
    let totalIncome = 0;
    let totalExpenses = 0;

    try {
        categoryLabels = JSON.parse(dashboardData.dataset.categories || "[]");
        categoryValues = JSON.parse(dashboardData.dataset.categoryValues || "[]");
        totalIncome = Number(dashboardData.dataset.income || 0);
        totalExpenses = Number(dashboardData.dataset.expenses || 0);
    } catch (error) {
        console.error("Unable to load dashboard chart data:", error);
        return;
    }

    /* Dark theme colors */
    const categoryColors = [
        "#f5c451", "#e8a92a", "#fff0b3", "#b8791a",
        "#d9b15a", "#8a5a0c", "#f7d98c", "#c98b1e"
    ];
    const textColor = "#c7bb9a";
    const mutedColor = "#a39878";
    const gridColor = "#2b2415";

    const rupees = (value) =>
        "₹" + Number(value).toLocaleString("en-IN", { minimumFractionDigits: 2 });

    /* EXPENSE CATEGORY DOUGHNUT */
    if (expenseCanvas) {
        new Chart(expenseCanvas, {
            type: "doughnut",
            data: {
                labels: categoryLabels,
                datasets: [{
                    data: categoryValues,
                    backgroundColor: categoryColors,
                    borderWidth: 2,
                    borderColor: "#060504",
                    hoverOffset: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: "65%",
                plugins: {
                    legend: {
                        position: "bottom",
                        labels: {
                            color: textColor,
                            usePointStyle: true,
                            pointStyle: "circle",
                            padding: 15,
                            font: { size: 11 }
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: (context) => " " + context.label + ": " + rupees(context.raw)
                        }
                    }
                }
            }
        });
    }

    /* INCOME VS EXPENSE BAR CHART */
    if (incomeExpenseCanvas) {
        new Chart(incomeExpenseCanvas, {
            type: "bar",
            data: {
                labels: ["Income", "Expenses"],
                datasets: [{
                    label: "Amount",
                    data: [totalIncome, totalExpenses],
                    backgroundColor: ["#f5c451", "#b8791a"],
                    borderRadius: 8,
                    borderSkipped: false,
                    maxBarThickness: 65
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: { display: false },
                        ticks: { color: mutedColor, font: { size: 11 } }
                    },
                    y: {
                        beginAtZero: true,
                        grid: { color: gridColor },
                        ticks: {
                            color: mutedColor,
                            font: { size: 10 },
                            callback: (value) => "₹" + Number(value).toLocaleString("en-IN")
                        }
                    }
                },
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: (context) => " " + rupees(context.raw)
                        }
                    }
                }
            }
        });
    }
}