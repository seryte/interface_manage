import {get_code, post_code, put_code} from "./common";

export const register = function (name, pwd) {
  return post_code("register", {name: name, pwd: pwd})
}


export const login = function (name, pwd) {
  return put_code("login", {name: name, pwd: pwd})
}

export const get_user = function (name, pwd) {
  return get_code("get_user")
}

