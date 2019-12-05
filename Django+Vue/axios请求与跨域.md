1. 创建一个django工程并运行

2. 运行vue工程

3. vue配置跨域

   - cd vueproject/src/main.js

     - 导入axios模块
     - import axios from ‘axios’
     - 注册axios模块
     - Vue.prototype.$axios = axios

   - cd vueproject/config/index.js

     - 配置跨域请求----—-proxytable

     - ```javascript
       proxyTable: {
           '/api': {
               target: 'http://127.0.0.1:8000/api/test/',
               #要连接的接口
               changeOrigin: true,
               #是否跨域
               pathRewrite: {
                   '^api/':''
                   #重写接口的域名
               }    
           }
       }
       ```

   - cd 到要发送跨域请求的vue文件

     - 设置跨域

     - ```
       export default {
           name:'User',
           data(){
               return {
                   page_info: 'this is user route'
               }
           },
           created(){
               this.$axios.get('http://127.0.0.1:8000/api/test').then(response => {console.log(response.data)})
           }
       }
       ```

   - 在将以上数据配置完之后,还会出现请求被拒绝的情况,这个时候需要对django项目进行设定

4. django项目内部设定方法

   - cd django/setting.py

     - ```python
       CORS_ALLOW_CREDENTIALS = True
       CORS_ORIGIN_ALLOW_ALL = True
       ```

   - 创建django跨域中间件

     - 在应用中创建middlewares.py文件

     - ```python
       from django.utils.deprecation import MiddlewareMixin
       class MyTest(MiddlewareMixin):
           def precess_response(self,request,response):
               response['Access-Control-Allow-Origin'] = ['*']
               return response
       ```

     - 注册中间件

     - ```
       'app.middlewares.MyTest'
       ```

5. 在完成了上述步骤之后,跨域请求的基本要求就完成了

6. 将获得数据绑定到vue模板中去

   - 在模板版中准备一个接受用的变量

     - ```
       django_message : ''
       ```

   - 在请求到数据之后将数据赋予这个变量

     - ```
       this.django_message = response.data.message
       ```

7. 