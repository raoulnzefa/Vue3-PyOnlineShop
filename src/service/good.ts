/*
 * @Descripttion: 商品列表
 * @Date: 2021-05-03 17:11:18
 * @LastEditTime: 2021-05-25 22:49:23
 */


import{get,post} from "@/utils/request";



/**
 * @name:查看图书内容
 */
 export function getGoodsList(params: any) {
    return get("/goods", params);
}


