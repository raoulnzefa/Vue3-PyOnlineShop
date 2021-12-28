<template>
  <!-- 首页公共部分 -->
  <div>
    <router-view name="head"> </router-view>
    <router-view name="content"></router-view>
    <router-view name="footer"></router-view>
    <!-- <br />
    <Hello /> -->
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";
// import Hello from "@/components/HelloWorld.vue";
let a = "1";
export default defineComponent({
  name: "App",
  components: {
    // Hello,
  },
});
</script>

<style lang="scss"></style>
