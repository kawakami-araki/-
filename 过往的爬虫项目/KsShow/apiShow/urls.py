from django.urls import path

from apiShow.views import Show_spider

urlpatterns = [
    path('',Show_spider.as_view({
        'get': 'list',
    })),
]
