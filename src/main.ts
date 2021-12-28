import { createApp } from 'vue'
import App from './App.vue'
import {router} from '@/router'


// 对应的样式
import '@/styles/common.scss';

const app = createApp(App);

app.use(router)
app.mount("#app");
