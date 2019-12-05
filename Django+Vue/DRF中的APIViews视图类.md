# from rest_framework.views import APIViews

1. 封装在DRF中的视图模块,相比直接使用django中的views模块,这个模块的使用更加的严谨,功能更多,更好用

   1. 从页面中使用request获取到的json数据将会自动转换成字典类型的数据,方便使用,不需要额外导入一次json模块
   2. 其他方面的使用views使用方式相同
   3. 从根本上来看,APIViews继承自Views

   

