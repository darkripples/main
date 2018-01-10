# coding:utf8

import traceback, json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F, Q
from .models import NoteContent, NoteUser, NoteType
from .Consts import PAGESIZE
from .forms import NoteContentForm
from fls_utils.utils import e_now

import logging
logger = logging.getLogger('django')
print = logger.info

def index(request):
    """ 首页展示 """
    # 当前页
    page = int(request.GET.get('page', '1') or 1)
    # 总页数
    allPage = int(request.GET.get('allPage', '1') or 1)
    # 翻页类型(上页/下页)
    pageType = request.GET.get('pageType','')
    # 查询条件
    note_type = request.GET.get('note_type','') or ''
    # 判断是点击上页/下页
    if pageType == 'pageDown':
        page += 1
    if pageType == 'pageUp':
        page -= 1
    context = {}
    startPos = (page-1) * PAGESIZE
    endPos = startPos + PAGESIZE
    
    # 根据查询条件组织获取结果集
    ## 可变查询条件
    q = Q()
    if note_type:
        # 类型
        q.add(Q(note_type=note_type), Q.AND )
    if not request.session.get('dr_user'):
        # 未登录，只展示公开类型的
        q.add( Q(isOpen='1'), Q.AND )
    else:
        # 已登录，展示自己的or别人公开的
        now_username = eval(request.session.get('dr_user')).get('user')
        q.add( Q(isOpen='1')|Q(author__user__username__exact=now_username), Q.AND)
    # 获取结果集
    blog_lists = NoteContent.objects.filter(q).order_by('-create_time')[startPos:endPos]
    if page == 1 and allPage == 1:
        # 第一次加载
        allPostCounts = blog_lists.count()
        # 总页数
        allPage = allPage//PAGESIZE if allPage%PAGESIZE==0 else allPage//PAGESIZE+1
    
    context['type_all'] = NoteType.objects.all()
    context['dr_user'] = request.session.get('dr_user')
    context['blog_lists'] = blog_lists
    context['page'] = int(page)
    context['allPage'] = allPage
    return render( request, 'blog/index.html', context )

def blog_detail(request):
    # 传的参数给url用
    try:
        context = {}
        blog_id = request.GET.get('id')
        blogDetail = NoteContent.objects.get(id=str(blog_id))
        NoteContent.objects.filter(id=str(blog_id)).update(view_count=F('view_count')+1)
        context['blogDetail'] = blogDetail
    except Exception as e:
        logger.error(repr(e))
        return render(request, '404.html')
    return render(request, 'blog/blog_detail.html', context)

@csrf_exempt
def add_blog(request):
    # 新增
    context = {'xym':'1'}
    if request.method == 'POST':
        # 登记数据
        content = request.POST.get('content')
        note_type = request.POST.get('note_type')
        title = request.POST.get('title')
        isOpen = request.POST.get('isOpen')
        form = NoteContentForm(request.POST)
        if form.is_valid():
            # 获取内容
            now_username = eval(request.session.get('dr_user'))
            author = NoteUser.objects.get(id=now_username['id'])
            now_time = e_now(fmt='%Y-%m-%d %H:%M:%S')
            new_models = NoteContent(
                title = title,
                note_type = note_type,
                note = content[:20],
                content = content,
                author = author,
                view_count = 0,
                create_time = now_time,
                update_at = now_time,
                isOpen = isOpen
            )
            new_models.save()
            context['xym'] = '0'
        else:
            context['errors'] = form.errors
        return HttpResponse( json.dumps( context ) )
    else:
        # 访问页面
        if not request.session.get('dr_user'):
            # 二次判断，未登录，不可新增
            return redirect('/')
    context['type_all'] = NoteType.objects.all()
    return render( request, 'blog/add_blog.html', context )

@csrf_exempt
def del_blog(request):
    # 删除
    context = {'flag':'fail'}
    try:
        if request.is_ajax() and request.method == 'POST':
            blog_id = request.POST.get('id')
            now_username = eval(request.session.get('dr_user','{}')).get('user')
            logger.debug("blog.views.del_blog.id=" + str(blog_id) + "|user=" + str(now_username))
            if now_username and blog_id:
                NoteContent.objects.get(id=str(blog_id)).delete()
                context['flag'] = 'succ'
    except Exception as e:
        logger.error(repr(e))
    return HttpResponse( json.dumps( context ) )
