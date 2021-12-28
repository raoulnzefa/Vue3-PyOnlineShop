/*
 * @Descripttion: 路由配置文件
 * @Date: 2021-05-26 20:33:07
 */

import {createRouter,createWebHistory} from "vue-router"

// 静态路由
const defaultRouter = [
    {
      path:'/',
      name:'首页',
      redirect:{name:'home'}
    },
    {
        path: "/app",
        name: "app",
        component:()=> import("@/pages/app/index.vue"),
        children:[
        {
          path:'login',
          name:'login',
          components:{
            head:()=>import('@/pages/head/index.vue'),
            content:()=>import('@/pages/home/index.vue'),
            footer:()=>import('@/pages/footer/index.vue'),
          },
          meta:{
            title:'登录',
            need_log:false
          }
        },
        // {},
        {
            path:'home',
            name:'home',
            components:{
              head:()=>import('@/pages/head/index.vue'),
              content:()=>import('@/pages/home/index.vue'),
              footer:()=>import('@/pages/footer/index.vue'),
            },
            children:[

            ]
        },
        {
          path:'shoppingcart',
          name:'home',
          components:{
            head:()=>import('@/pages/head/index.vue'),
            content:()=>import('@/pages/home/index.vue'),
            footer:()=>import('@/pages/footer/index.vue'),
          }
        }
        ]
    },

]


// 路由信息
const routes = [...defaultRouter];

// 导出路由
const router = createRouter({
    history: createWebHistory(),
    routes,
  });

//   // 前置路由
// router.beforeEach((to,from,next)=>{
//     console.log(to);
//     console.log(from)
//     if(to.path === "/"){
//         console.log(111)
//         next({
//             path: '/app',
//         });
//     }
// })
export {router}