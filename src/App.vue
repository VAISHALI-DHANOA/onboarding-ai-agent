<template>
<div style="width: 90%; margin: auto; padding: 20px;">
  <h1 class="text-2xl font-bold mb-4">Interactive Dashboard</h1>
    <Filters @update-filter="updateFilter" />
    <div class="grid grid-cols-2 gap-4">
      <BarChart :data="filteredData" />
      <LineChart :data="filteredData" />
      <DataTable :data="filteredData" />
    </div>
    <div>
      <HomeView/>
    </div>
  </div>
</template>

<script>
import BarChart from './components/BarChart.vue';
import LineChart from './components/LineChart.vue';
import DataTable from './components/DataTable.vue';
import Filters from './components/Filters.vue';
import HomeView from './HomeView.vue';

export default {
  components: { BarChart, LineChart, DataTable, Filters, HomeView },
  data() {
    return {
      data: [], // Full dataset
      filteredData: [], // Filtered dataset
      filter: null, // Filter criteria
    };
  },
  methods: {
    updateFilter(criteria) {
      this.filter = criteria;
      this.filteredData = this.data.filter((item) =>
        // Update this filter logic based on your data
        item.category === criteria
      );
    },
  },
  mounted() {
    // Fetch or initialize data
    this.data = [
      { category: 'A', value: 30 },
      { category: 'B', value: 50 },
      { category: 'C', value: 70 },
    ];
    this.filteredData = this.data;
  },
};
</script>
