# package.json
> 项目信息，依赖文件，命令定义等

# node_modules
> 依赖文件

# public
> 外部静态文件

# src
> assets  #  资源文件
> components  #  组件文件
> requests  # 请求
> router  #  路由定义

# App.vue
> 入口vue文件，所有页面都从这个文件延申出来

# main.js
> 项目主文件，理解成C语言的main()函数


# 执行顺序
* main.js
* ruote/index.js
* App.vue

# vue文件三层结构
* html
```html
# 固定格式
<tempalte>
    <div>
         for example
    </div>
</tempalte>

```
* script
```html
<script>
  import interface_png from './assets/interface.png'

  export default {
    name: 'App',
    data() {
      return {
        head_img: interface_png,
      }
    }
  }
</script>

```
* css



 ## 以下是自动生成的
# my_project

> A Vue.js project

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
