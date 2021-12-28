/**
 *  author:lifechat
 *  desc:获取对应的url参数
 * */ 


 export const  getQueryString = (name) => {
    console.log(name);
    let reg = new RegExp("(^|&)"+name+"");
    let r = window.location.search;
    console.log(r);
};
  