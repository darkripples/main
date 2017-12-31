# coding:utf8
"""dr_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
"""
import os
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic.base import RedirectView
from oa import views, main
from django.views.generic import TemplateView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=r'/static/img/favicon.ico')),
    path('admin_fls/', admin.site.urls),
    path('',main.login ),
    ##################
    # About Login
    path('login/',main.login, name="login" ),
    path('logout/',main.logout_view, name="logout" ),
    path('register/',main.register_view, name="register" ),
    ##################
    # blog
    path('blog/',include('blog.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
