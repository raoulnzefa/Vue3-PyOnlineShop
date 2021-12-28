<script lang="ts">
import { onMounted, toRefs, reactive } from "vue";
import { getGoodsList } from "@/service/good";

export default {
  name: "helloworld",
  setup: () => {
    const state = reactive({
      list: [],
    });

    const getList = async () => {
      const res: any = await getGoodsList({});
      console.log(res);
    };
    onMounted(getList);
    return {
      ...toRefs(state),
    };
  },
};
</script>

<template>Ts+vue3+vite</template>

<style scoped>
a {
  color: #42b983;
}

label {
  margin: 0 0.5em;
  font-weight: bold;
}

code {
  background-color: #eee;
  padding: 2px 4px;
  border-radius: 4px;
  color: #304455;
}
</style>
