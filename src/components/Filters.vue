<template>
  <div class="mb-4">
    <label for="filter" class="block font-medium text-gray-700 mb-1">Select Category:</label>
    <select id="filter" class="p-2 border border-gray-300 rounded" @change="applyFilter">
      <option value="">All</option>
      <option v-for="option in options" :key="option" :value="option">{{ option }}</option>
    </select>
  </div>
</template>

<script>
export default {
  props: [],
  data() {
    return {
      options: ['A', 'B', 'C'], // Update with dynamic categories if needed
    };
  },
  methods: {
    applyFilter(event) {
      this.$emit('update-filter', event.target.value);
    },
  },
};
</script>
