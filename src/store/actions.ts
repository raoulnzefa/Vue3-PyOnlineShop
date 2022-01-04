import * as types from './mutation-types';

function makeAction(type:any):any{
    return ({commit},...args) => commit(type,...args)
}


export const setInfo = makeAction(types.SET_INFO);
export const setNav = makeAction(types.SET_NAV);

export const setShopList = makeAction(types.SET_SHOPLIST);