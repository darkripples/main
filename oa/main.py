# coding:utf8

import json, os
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect

from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from .forms import DRUserForm
from blog.models import NoteUser, IMG

@csrf_exempt
def login( req ):
    context = {}
    if req.method == 'POST':
        form = DRUserForm(req.POST)
        if form.is_valid():
            #获取表单用户密码
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #获取的表单数据与数据库进行比较
            user = authenticate(username = username,password = password)
            if user:
                #比较成功，跳转index
                auth.login(req, user)
                req.session['user'] = NoteUser.objects.get(user=user.id).toJSON()
                context = {'isLogin': True}
                return redirect('/')
            else:
                #比较失败，还在login
                context = {'isLogin': False,'pawd':False}
                return render(req, 'login.html', context)
    else:
        if req.session.get('user'):
            # 已登录
            context = {'isLogin': True}
            return redirect('/blog/')
        else:
            context = {'isLogin': False,'pswd':True}
    return render(req, 'login.html', context)

#登出
def logout_view(req):
    #清理cookie里保存user
    context = {}
    auth.logout(req)
    return render(req, 'login.html', context)

#注册
@csrf_exempt
def register_view(req):
    context = {}
    if req.method == 'POST':
        form = DRUserForm(req.POST)
        if form.is_valid():
            #获得表单数据
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # 判断用户是否存在
            user = auth.authenticate(username = username,password = password)
            if user:
                context['userExit']=True
                return render(req, 'register.html', context)


            #添加到数据库（还可以加一些字段的处理）
            user = User.objects.create_user(username=username, password=password)
            user.save()

            #添加到session
            req.session['user'] = user
            #调用auth登录
            auth.login(req, user)
            #重定向到首页
            return redirect('/blog/')
    else:
        context = {'isLogin':False}
    #将req 、页面 、以及context{}（要传入html文件中的内容包含在字典里）返回
    return  render(req, 'register.html', context)

@csrf_exempt
def uploadFile(req):
    # 上传
    ret_dic = {'msg':'error'}
    if req.method == 'POST':
        if req.FILES.get('file'):
            imgObj = req.FILES.get('file')
            imgName = req.FILES.get('file').name
            new_img = IMG(
                img = imgObj,
                name = imgName,
                type = req.POST.get("type","blog")
            )
            new_img.save()
        ret_dic['msg'] = os.path.join('/', settings.UPLOAD_IMG_URL, imgName)
    return HttpResponse( json.dumps( ret_dic ) )



