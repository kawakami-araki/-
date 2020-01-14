# from rest_framework.routers import DefaultRouter
# from .views import *
# urlpatterns = []
# router = DefaultRouter()
# router.register('students',StudentsAPIViews,basename='StudentsAPIViews')
# urlpatterns += router.urls
from django.urls import path,re_path
from .views import list
urlpatterns = [
    path('baijuyi/', list)
]
