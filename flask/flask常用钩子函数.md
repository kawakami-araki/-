# 常用钩子函数

1. ### errorhandler

   1. 错误报告专用

   2. 在装饰器中传入参数进行对应错误代码进行捕获

   3. 定义错误捕获函数进行捕获,此函数中定义参数为error

   4. 此错误报告可以返回 'html' 页面,并使用js对其进行修饰

      1. 使用abort模块进行错误跳转,即,当访问的界面不符合条件时,直接返回对应的错误,

         1. ```python
            from flask import abort
            
            .....
            @app.route('/)
            def func():
            	if....:
                   return render_template('...html')
                else:
                   #不满足条件直接返回404错误
                   abort(404)
            ```

            

   - ```python
     @app.errorhandler(404)
     def func1(error):
         return '404'
     @app.errorhandler(500)
     def func2(error):
         return '500'
     ```

2. ### context_processor

   1. 上下文声明专用
   2. 在声明的函数中直接返回要定义的上下文内容

   - ```python
     @app.context_processor
     def function():
         return {"current":""}
     ```