"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    定义视图函数相关的URL(网址)  （即规定 访问什么网址对应什么内容）
"""
from django.contrib import admin
from django.urls import path
from learn import views as learn_views  # new

urlpatterns = [
    path("add/", learn_views.add),  # 加法运算
    path("", learn_views.index),  # new 此时不要加括号，直接方法名称即可
    path('admin/', admin.site.urls),
]
