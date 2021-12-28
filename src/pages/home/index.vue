<script lang="ts">
import { onMounted, toRefs, reactive } from "vue";
import { getGoodsList } from "@/service/good";
import { getQueryString } from "@/router/getQueryString";

export default {
  name: "home",
  setup: () => {
    const state = reactive({
      list: [],
    });
    getQueryString("name");

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

<template>
  <div class="middle">我是内容组件</div>
</template>

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
.middle {
  height: 80vh;
  width: 100vw;
  background: skyblue;
}
</style>
