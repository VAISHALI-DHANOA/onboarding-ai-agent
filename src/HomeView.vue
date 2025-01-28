<script setup lang="ts">
import { useRouter } from 'vue-router' // Import useRouter from vue-router
import RadialMenu from '../src/components/RadialMenu.vue'
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps({
  selectedOption: {
    type: Object as () => { name: string; icon: string; submenu: string[] },
    required: true,
  },
}) // Create a router instance
const router = useRouter()

// Create a reactive reference for radial menu options
const radialMenuOptions = ref([
  { name: 'Data', icon: 'description', submenu: ['Submenu 1', 'Submenu 2', 'Submenu 3'] },
  { name: 'Insight', icon: 'visibility', submenu: ['Submenu 1', 'Submenu 2', 'Submenu 3'] },
  { name: 'Interaction', icon: 'mouse', submenu: ['Submenu 1', 'Submenu 2', 'Submenu 3'] },
  { name: 'Usage', icon: 'school', submenu: ['Submenu 1', 'Submenu 2', 'Submenu 3'] },
])

// Reactive property for the radial menu's visibility and position
const radialMenuVisible = ref(false)
const radialMenuPosition = ref({ x: 0, y: 0 })

// Function to handle global click events
const handleClick = (event: MouseEvent) => {
  radialMenuVisible.value = true
  radialMenuPosition.value = { x: event.clientX, y: event.clientY }
}

// Function to dynamically update radial menu options
const updateRadialMenu = () => {
  radialMenuOptions.value = [
    { name: 'Profile', icon: 'person', submenu: ['Submenu 1', 'Submenu 2', 'Submenu 3'] },
    { name: 'Messages', icon: 'message', submenu: ['Submenu 1', 'Submenu 2', 'Submenu 3'] },
  ]
}

// Function to handle the click event
const navigateToEditor = () => {
  router.push('/editor') // Navigate to /editor
}

// Attach click event listener on mount
onMounted(() => {
  document.addEventListener('click', handleClick)
})

// Clean up the event listener on unmount
onUnmounted(() => {
  document.removeEventListener('click', handleClick)
})
</script>

<template>
  <main>
    <!-- RadialMenu Component -->
    <RadialMenu
      v-if="radialMenuVisible"
      :options="radialMenuOptions"
      :selectedOption="selectedOption"
      :x="radialMenuPosition.x"
      :y="radialMenuPosition.y"
    />
  </main>
</template>

<style scoped>
main {
  display: flex;
  background-color: #f0f0f0;
}

/* RadialMenu dynamic styling */
.radial-menu {
  position: absolute;
  z-index: 1000;
}
</style>
