# coding:utf8

from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView

from fls_utils.utils import e_now
from fls_utils.fls_log import fls_log

log = fls_log( settings.LOGS_DIR + ('/oa.views.log.%s'%e_now()[:6]) )

def idx( req ):
    """
    测试idx
    """
    log.log_info('11212')
    return render(req, "test/test.html", {'fls': 'fls'})

class TestView(TemplateView):
    template_name = 'test/test.html'
    
    
