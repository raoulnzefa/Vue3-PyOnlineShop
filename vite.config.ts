import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import {resolve} from 'path';


// https://vitejs.dev/config/

export default ({mode}) => {
  //是否是开发环境
  const __DEV__ = mode === "development";

  return defineConfig({
    css:{
      // 配置样式
     
    },
    resolve:{
      extensions: [".js", ".vue", ".json", ".ts"],
      alias:{
        "@": resolve(__dirname, "src"),
        '~':resolve(__dirname,'src/components'),
        '#':resolve(__dirname,'src/views'),
        '*':resolve(__dirname,'src/assets'),
      }
    },
    server:{
      // 服务器主机名，如果允许外部访问，可设置为"0.0.0.0"
      // host:"0.0.0.0",
      // 服务器端口号
      port:3000,
      // boolean | string 启动项目时自动在浏览器打开应用程序；如果为string，比如"/index.html"，会打开http://localhost:3000/index.html
      open:true,
      // 自定义代理规则
      proxy:{
        '/api':{
            target: "http://127.0.0.1:8000",
          // target: "http://localhost:3001",
        }
      }
    },
    plugins: [
      vue(),
    ],
  })
}

