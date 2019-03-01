let host = "http://127.0.0.1:8000/"

let request_ = function (url, params) {
  let body = JSON.stringify(params);
  return fetch(host + url, {
    method: "GET",
    credentials: "include",
  }).then(respone=> {
    return respone
  })
}

export const login = function (name, pwd) {
  return request_("login", {name: name, pwd: pwd})
}
