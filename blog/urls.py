# coding:utf8
"""blog URL Configuration
"""

from django.urls import path
from django.views.generic import TemplateView

from blog import views
from oa.main import uploadFile

urlpatterns = [
    path('', views.index, name='index'),
    # View Detail
    path('blog_detail/', views.blog_detail, name='blog_detail'),
    # add
    path('add_blog/', views.add_blog, name='add_blog'),
    # del
    path('del_blog/', views.del_blog, name='del_blog'),
    # UploadFile
    path('uploadFile/', uploadFile, name='uploadFile'),
]


