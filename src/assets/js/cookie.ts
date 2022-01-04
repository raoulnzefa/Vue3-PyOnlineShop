//设置cookie,增加到vue实例方便全局调用
//vue全局调用的理由是，有些组件所用到的接口可能需要session验证，session从cookie获取
//当然，如果session保存到vuex的话除外
//全局引入vue
const cookie = {
    setCookie(){

    },
    getCookie(){

    },
    delCookie(){

    }
}

export default cookie;