#！-*-coding：UTF-8-*-

from django.conf.urls import url,include
from django.contrib import admin
from online import views

app_name = 'online' #为 URL 名称添加命名空间

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$',views.login,name = 'login'),
    url(r'^regist/$',views.regist,name = 'regist'),
    url(r'^index/$',views.index,name = 'index'),
    url(r'^logout/$',views.logout,name = 'logout'),
]