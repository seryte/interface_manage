let host = "http://127.0.0.1:8000/"

let get_code = function (url, params) {
  let body = JSON.stringify(params);
  return fetch(host + url, {
    method: "GET",
    credentials: "include",
  }).then(respone=> {
    return respone.json()
  })
};


let post_code = function (url, params) {
  let body = JSON.stringify(params);
  return fetch(host+url, {
    method: "POST",
    credentials: "include",
    body: body,
  }).then(respone=> {
    return respone.json()
  })
};


export const register = function (name, pwd) {
  return post_code("register", {name: name, pwd: pwd})
}


export const login = function (name, pwd) {
  return post_code("login", {name: name, pwd: pwd})
}
