import VueCookies from "vue-cookies";

let host = "http://127.0.0.1:8000/"

export const get_code = function (url) {
  return fetch(host + url, {
    method: "GET",
    credentials: "include",
    headers: {
      "token": VueCookies.get("token")
    }
  }).then(respone => {
    return respone.json()
  })
};


export const post_code = function (url, params) {
  let body = JSON.stringify(params);
  return fetch(host + url, {
    method: "POST",
    credentials: "include",
    body: body,
    headers: {
      "token": VueCookies.get("token")
    }
  }).then(respone => {
    return respone.json()
  })
};

export const put_code = function (url, params) {
  let body = JSON.stringify(params);
  return fetch(host + url, {
    method: "PUT",
    credentials: "include",
    body: body,
    headers: {
      "token": VueCookies.get("token")
    }
  }).then(respone => {
    return respone.json()
  })
};

