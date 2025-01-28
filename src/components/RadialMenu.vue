<template>
  <head>
    <link
      href="https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Round|Material+Icons+Sharp|Material+Icons+Two+Tone"
      rel="stylesheet"
    />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@200;300;400;500;600;700;800&family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap"
      rel="stylesheet"
    />
  </head>
  <!-- <div class="menu" :style="{ top: y + 'px', left: x + 'px', position: 'absolute' }">
    <a v-for="(option, index) in options" :key="index" href="">
      <div class="sector" :style="sectorStyles[index]"></div>
      <div class="option" :style="optionStyles[index]">
        <span class="material-icons-round">{{ option.icon }}</span>
        <div class="name">{{ option.name }}</div>
        <div class="submenu" :style="optionStyles[index].submenuClass>
          <a v-for="(subOption, subIndex) in option.submenu" :key="subIndex" href="">
            {{ subOption }}
          </a>
        </div>
      </div>
    </a>
  </div>
</template> -->

  <div class="menu" :style="{ top: y + 'px', left: x + 'px', position: 'absolute' }">
    <a v-for="(option, index) in options" :key="index" href="">
      <div class="sector" :style="sectorStyles[index]"></div>
      <div class="option" :style="optionStyles[index]">
        <span class="material-icons-round">{{ option.icon }}</span>
        <div class="name">{{ option.name }}</div>
        <!-- Submenu -->
        <div
          v-if="option.submenu && option.submenu.length"
          class="submenu"
          :class="optionStyles[index].submenuClass"
        >
          <a v-for="(subOption, subIndex) in option.submenu" :key="subIndex" href="">
            {{ subOption }}
          </a>
        </div>
      </div>
    </a>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue'

export default defineComponent({
  name: 'RadialMenu',
  props: {
    options: {
      type: Array as () => { name: string; icon: string; submenu: string[] }[],
      required: true,
    },
    x: {
      type: Number,
      required: true,
      default: 0,
    },
    y: {
      type: Number,
      required: true,
      default: 0,
    },
  },
  setup(props) {
    // Reactive State
    const totalSectors = computed(() => props.options.length)
    const skewVal = computed(() => 360 / totalSectors.value - 90)
    const deviation = computed(() =>
      (totalSectors.value / 2) % 2 !== 0 ? 360 / totalSectors.value / 2 : 0,
    )

    // Dynamic Styles for Sectors
    const sectorStyles = computed(() =>
      props.options.map((_, index) => {
        const angle = (360 / totalSectors.value) * (index + 1) - deviation.value
        return {
          transform: `rotate(${angle}deg) skew(${skewVal.value}deg)`,
        }
      }),
    )

    // Dynamic Styles for Options
    const optionStyles = computed(() =>
      props.options.map((_, index) => {
        const angle = (360 / totalSectors.value) * (index + 1) - deviation.value
        const optionAngle = angle + Math.abs(skewVal.value) + (90 - Math.abs(skewVal.value)) / 2
        const submenuPosition = angle > 180 ? 'left' : 'right'

        return {
          transform: `rotateZ(${optionAngle}deg) translateY(-100px) rotate(-${optionAngle}deg)`,
          submenuClass: submenuPosition,
        }
      }),
    )

    return {
      sectorStyles,
      optionStyles,
    }
  },
})
</script>

<style scoped>
.menu {
  position: relative;
  width: 300px;
  height: 300px;
  border-radius: 50%;
  overflow: hidden;
  background: radial-gradient(
      55% 55% at 70% 35%,
      rgba(255, 255, 255, 0.2) 0%,
      rgba(0, 0, 0, 0) 100%
    ),
    rgba(255, 255, 255, 0.05);
  border: 2px solid rgba(255, 255, 255, 0.1);
  box-shadow:
    inset 2px 2px 2px rgba(255, 255, 255, 0.5),
    inset -1px -1px 1px rgba(255, 255, 255, 0.3);
}
.menu a {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.sector {
  width: 150px;
  height: 150px;
  transform-origin: 0 100%;
  margin-top: -150px;
  margin-right: -150px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.option {
  position: absolute;
  width: 80px;
  height: 50px;
  text-align: center;
  top: calc(50% - 30px);
  left: calc(50% - 50px);
  text-decoration: none;
  font-family: poppins;
  font-size: 10px;
  font-weight: 500;
  color: white;
  line-height: 20px;
  z-index: 1;
}
.menu a .option span {
  font-size: 25px;
}
.menu a:hover .sector {
  background: rgb(235, 85, 200);
}
.menu a:hover .option {
  color: black;
}
.menu::before {
  position: absolute;
  content: 'menu';
  font-family: 'Material Icons';
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 8px;
  height: 8px;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  z-index: 1;
}
.submenu {
  position: absolute;
  top: 100%;
  left: 50%;
  transform: translateX(-50%); /* Center vertically */
  background: rgba(0, 0, 0, 0.8);
  padding: 10px;
  border-radius: 5px;
  display: none;
  flex-direction: column;
  gap: 8px; /* Added gap between submenu items */
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.6); /* Optional: add shadow for better visibility */
  min-width: 120px; /* Minimum width to avoid very narrow submenus */
  z-index: 1000; /* Ensure it's on top of other elements */
}

.submenu a {
  color: rgb(94, 8, 206);
  text-decoration: none;
  font-size: 12px;
  padding: 8px 12px;
  border-radius: 3px;
  transition: background 0.2s;
}

.submenu a:hover {
  background: rgba(85, 187, 22, 0.2);
}

/* Position the submenu to the right or left */
.right .submenu {
  left: 100%;
  top: 50%; /* Center vertically */
}

.left .submenu {
  right: 100%;
  top: 50%; /* Center vertically */
}
.option:hover .submenu {
  display: flex;
}
</style>
