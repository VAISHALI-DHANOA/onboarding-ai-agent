<template>
  <table class="table-auto w-full bg-white border-collapse border border-gray-200">
    <thead>
      <tr class="bg-gray-100">
        <th class="border border-gray-200 px-4 py-2">Category</th>
        <th class="border border-gray-200 px-4 py-2">Value</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="row in data" :key="row.category">
        <td class="border border-gray-200 px-4 py-2">{{ row.category }}</td>
        <td class="border border-gray-200 px-4 py-2">{{ row.value }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ['data'],
};
</script>
