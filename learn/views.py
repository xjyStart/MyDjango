# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 第一行是声明编码为utf-8, 因为我们在代码中用到了中文,如果不声明就报错.

def index(request):
    return HttpResponse(u"欢迎光临！我的夏");


# 加法运算
def add(request):
    # a = request.GET['a']
    # b = request.GET['b']
    a = request.GET.get('a', 3)  # 默认值
    b = request.GET.get('b', 3)  # 默认值
    c = int(a) + int(b)
    return HttpResponse(str(c))
