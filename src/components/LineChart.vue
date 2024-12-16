<template>
  <div>
    <h2 class="text-xl font-bold mb-4">Line Chart</h2>
    <canvas ref="lineChart"></canvas>
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
    filteredCategories: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      filteredData: [],
    };
  },
  mounted() {
    this.updateFilteredData();
    this.renderChart();
  },
  watch: {
    data: 'updateFilteredData',
    filteredCategories: 'updateFilteredData',
    filteredData: 'renderChart',
  },
  methods: {
    updateFilteredData() {
      this.filteredData = this.filteredCategories.length
        ? this.data.filter((item) => this.filteredCategories.includes(item.category))
        : this.data;
    },
    renderChart() {
      const ctx = this.$refs.lineChart.getContext('2d');

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
        type: 'line',
        data: {
          labels: this.filteredData.map((item) => item.category),
          datasets: [
            {
              label: 'Values',
              data: this.filteredData.map((item) => item.value),
              backgroundColor: colors.slice(0, this.filteredData.length),
              borderColor: borderColors.slice(0, this.filteredData.length),
              borderWidth: 1,
              fill: false,
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
  },
};
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}
</style>
