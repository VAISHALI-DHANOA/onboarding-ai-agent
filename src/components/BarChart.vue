<template>
    <div style="width: 100%; height: 100%;">
      <canvas ref="barChart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart, registerables } from 'chart.js';
  Chart.register(...registerables);
  
  export default {
    props: {
      data: {
        type: Array,
        default: () => [
          { category: 'Red', value: 12 },
          { category: 'Blue', value: 19 },
          { category: 'Yellow', value: 3 },
          { category: 'Green', value: 5 },
          { category: 'Purple', value: 2 },
          { category: 'Orange', value: 8 },
        ],
      },
    },
    data() {
      return {
        options: [],
        filteredData: [],
      };
    },
    mounted() {
      this.options = [...new Set(this.data.map((item) => item.category))];
      this.filteredData = this.data;
      this.renderChart();
    },
    watch: {
      data(newData) {
        this.options = [...new Set(newData.map((item) => item.category))];
        this.filteredData = newData;
        this.renderChart();
      },
      filteredData: 'renderChart',
    },
    methods: {
      renderChart() {
        const ctx = this.$refs.barChart.getContext('2d');
  
        if (this.chart) {
          if (this.chart.destroy) {
            this.chart.destroy();
          }
        }
  
        const colors = [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
        ];
  
        const borderColors = [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ];
  
        this.chart = new Chart(ctx, {
          type: 'bar',
          data: {
            labels: this.filteredData.map((item) => item.category),
            datasets: [
              {
                label: 'Values',
                data: this.filteredData.map((item) => item.value),
                backgroundColor: colors.slice(0, this.filteredData.length),
                borderColor: borderColors.slice(0, this.filteredData.length),
                borderWidth: 1,
              },
            ],
          },
          options: {
            responsive: true,
            plugins: {
              legend: {
                display: true,
                position: 'top',
              },
              tooltip: {
                callbacks: {
                  label: (tooltipItem) => {
                    const value = tooltipItem.raw;
                    if (typeof value !== 'number') {
                      return 'Invalid value';
                    }
                    return `Value: ${value}`;
                  },
                },
              },
            },
            onClick: (event, elements) => {
              if (elements.length > 0) {
                const index = elements[0].index;
                const category = this.filteredData[index].category;
                const value = this.filteredData[index].value;
                alert(`Category: ${category}, Value: ${value}`);
              }
            },
            scales: {
              y: {
                beginAtZero: true,
                title: {
                  display: true,
                  text: 'Value',
                },
              },
              x: {
                title: {
                  display: true,
                  text: 'Category',
                },
              },
            },
          },
        });
      },
      applyFilter(event) {
        const selectedCategory = event.target.value;
        this.filteredData = selectedCategory
          ? this.data.filter((item) => item.category === selectedCategory)
          : this.data;
      },
    },
  };
  </script>
  
  <style scoped>
  canvas {
    max-width: 100%;
    height: auto;
  }
  </style>
  