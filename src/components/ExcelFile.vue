<template>
  <div>
    <canvas ref="lineChart"></canvas>
  </div>
</template>

<script>
import * as XLSX from 'xlsx'
import { Chart } from 'chart.js'

export default {
  name: 'LineChart',
  props: {
    excelFile: {
      type: File,
      required: true,
    },
    filteredCategories: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
      rawData: [],
      filteredData: [],
      chart: null,
    }
  },
  mounted() {
    this.loadExcelData()
  },
  watch: {
    rawData: 'updateFilteredData',
    filteredCategories: 'updateFilteredData',
    filteredData: 'renderChart',
  },
  methods: {
    async loadExcelData() {
      if (!this.excelFile) return

      try {
        const data = await this.excelFile.arrayBuffer()
        const workbook = XLSX.read(data, { type: 'array' })
        const sheetName = workbook.SheetNames[0]
        const worksheet = workbook.Sheets[sheetName]
        const jsonData = XLSX.utils.sheet_to_json(worksheet)

        this.rawData = jsonData.map((row) => ({
          category: row.Category || 'Unknown',
          value: row.Value || 0,
        }))
      } catch (error) {
        console.error('Error reading Excel file:', error)
      }
    },
    updateFilteredData() {
      this.filteredData = this.filteredCategories.length
        ? this.rawData.filter((item) => this.filteredCategories.includes(item.category))
        : this.rawData
    },
    renderChart() {
      const ctx = this.$refs.lineChart.getContext('2d')

      if (this.chart) {
        this.chart.destroy()
      }

      const colors = [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)',
      ]

      const borderColors = [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)',
      ]

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
      })
    },
  },
}
</script>

<style scoped>
canvas {
  max-width: 100%;
  height: auto;
}
</style>
