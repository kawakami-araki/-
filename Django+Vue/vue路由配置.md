# 配置vue路由

1. ## 第一步

   - cd ./vueproject/src/router

   - 进入到路由文件夹中,打开index.js文件

   - 在文件中导入设定好的Vue路由文件

     - import User from ‘../components/User’
     - 这里可以通过输入vue文件名的方式进行快捷编写

   - 在路由数组中注册路由

     - ```javascript
       routes: [
           {
               path:'/user',
               name: 'User',
               component:User
           }
       ]
       ```

   - 在app.vue文件中建立路由链接

     - ```
       <router-link to='/user'>user<router-link>
       ```

     - 这是一个超链接形式的标签

     ------

     ## 路由参数传递

     

传递参数时,将参数放在路由链接后面

使用:to的方法绑定路由文件

name为路由文件的名字,params为要传递的参数,以字典的形式传递

```javascript
<router-link :to="{ name:'User',params:{ username : 'root' } }" >user</router-link>
```

渲染:

使用模板语法,对传递过来的参数进行提取

{{ $route.params.username }}

