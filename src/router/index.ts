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
      redirect:{name:'home'},
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
              content:()=>import('@/pages/login/index.vue'),
              footer:()=>import('@/pages/footer/index.vue'),
            },
            meta:{
              title:'登录',
              need_log:false
            }
          },
          {
            path: 'register',
            name: 'register',
            components:{
              head:()=>import('@/pages/head/index.vue'),
              content:()=>import('@/pages/home/index.vue'),
              footer:()=>import('@/pages/footer/index.vue'),
            },
            meta:{
              title:'注册',
            }
          },
          {
              path:'home',
              name:'home',
              components:{
                head:()=>import('@/pages/head/index.vue'),
                content:()=>import('@/pages/home/index.vue'),
                footer:()=>import('@/pages/footer/index.vue'),
              },
              children:[

              ],
              meta:{
                title:'商城首页'
              }
          },
          {
            path:'shoppingcart',
            name:'shoppingcart',
            components:{
              head:()=>import('@/pages/head/index.vue'),
              content:()=>import('@/pages/home/index.vue'),
              footer:()=>import('@/pages/footer/index.vue'),
            },
            children:[
              {
                path:'cart',
                name:'cart',
                component:()=>import('@/pages/cart/index.vue'),
                meta:{
                  title:'购物车'
                }
              }
            ]
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
// houzhi
// 修改跳转路由的标题
router.afterEach((to,from,next)=>{
  document.title = to.matched[to.matched.length-1].meta.title;
})

// 抛出路由
export {router}