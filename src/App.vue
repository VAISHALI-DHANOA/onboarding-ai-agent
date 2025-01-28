<template>
  <div style="width: 90%; margin: auto; padding: 20px">
    <h1 class="text-2xl font-bold mb-4">Interactive Dashboard</h1>
    <Filters @update-filter="updateFilter" />
    <div class="grid grid-cols-2 gap-4">
      <BarChart :data="filteredData" />
      <LineChart :data="filteredData" />
      <!-- <div v-if="!excelFile">Loading Excel File...</div>
      <ExcelFile v-else :excelFile="excelFile" :filteredCategories="['Red', 'Blue']" /> -->
      <!-- <ExcelFile :excelFile="excelFile" :filteredCategories="['Red', 'Blue']" /> -->
      <DataTable :data="filteredData" />
    </div>
    <div>
      <HomeView />
    </div>
  </div>
</template>
<script>
import BarChart from './components/BarChart.vue'
import LineChart from './components/LineChart.vue'
import DataTable from './components/DataTable.vue'
import Filters from './components/Filters.vue'
import HomeView from './HomeView.vue'
import ExcelFile from './components/ExcelFile.vue'
import FinanceData from './assets/FinanceData.xlsx'

export default {
  components: { BarChart, DataTable, Filters, LineChart, HomeView },
  data() {
    return {
      data: [], // Full dataset
      filteredData: [], // Filtered dataset
      filter: null, // Filter criteria
      excelFile: null,
    }
  },
  async created() {
    try {
      const response = await fetch(FinanceData) // Fetch the file as a static asset
      const blob = await response.blob()
      this.excelFile = new File([blob], 'FinanceData.xlsx')
      console.log('Found the file', this.excelFile)
    } catch (error) {
      console.error('Error loading Excel file:', error)
    }
  },
  methods: {
    updateFilter(criteria) {
      this.filter = criteria
      this.filteredData = this.data.filter(
        (item) =>
          // Update this filter logic based on your data
          item.category === criteria,
      )
    },
  },
  async mounted() {
    // Fetch or initialize data
    this.data = [
      { category: 'A', value: 30 },
      { category: 'B', value: 50 },
      { category: 'C', value: 70 },
    ]
    this.filteredData = this.data
    // Make a request for a user with a given ID
    const prompt = 'Can you filter the graph?'
    const myresponse = await fetch('http://127.0.0.1:8000/handle_interaction/' + prompt + '}', {
      method: 'GET',
    })
    const data = await myresponse.json()
    console.log('Success', data)
  },
}
</script>
