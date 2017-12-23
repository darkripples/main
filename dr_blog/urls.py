"""dr_blog URL Configuration

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
from django.urls import path
from django.conf import settings

from oa import views, main
from django.views.generic import TemplateView

urlpatterns = [
    path('admin_fls/', admin.site.urls),
    #path('', TemplateView.as_view(template_name='index.html'), name="home"),
    path('', views.HomePageView.as_view(), name='home'),
    path('formset', views.DefaultFormsetView.as_view(), name='formset_default'),
    path('form', views.DefaultFormView.as_view(), name='form_default'),
    path('form_by_field', views.DefaultFormByFieldView.as_view(), name='form_by_field'),
    path('form_horizontal', views.FormHorizontalView.as_view(), name='form_horizontal'),
    path('form_inline', views.FormInlineView.as_view(), name='form_inline'),
    path('form_with_files', views.FormWithFilesView.as_view(), name='form_with_files'),
    path('pagination', views.PaginationView.as_view(), name='pagination'),
    path('misc', views.MiscView.as_view(), name='misc'),
    # test
    path('test', main.TestView.as_view(), name='test'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
