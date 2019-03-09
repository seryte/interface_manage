import {get_code, post_code, put_code} from "./common";

export const register = function (name, pwd) {
  return post_code("register", {username: name, password: pwd})
}


export const login = function (name, pwd) {
  return put_code("login", {username: name, password: pwd})
}

export const get_user = function () {
  return get_code("get_user")
}

