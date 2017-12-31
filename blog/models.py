# conding:utf8
import datetime
from django.db import models
from django.contrib.auth.models import User  #导入django自带的用户
from django.conf import settings

class NoteContent(models.Model):
    """ 帖子内容表 """
    # 标题
    title = models.CharField(max_length=50)
    # 帖子类型模块
    note_type = models.CharField(max_length=30)
    # 摘要。可以为空，blank是admin中可为空，null是表里可为空
    note = models.CharField(max_length=200,blank=True,null=True)
    # 内容
    content = models.TextField()
    # 作者，外键到BBS_user中，用到还未定义的表要用引号
    author = models.ForeignKey( 'NoteUser', on_delete=models.CASCADE )
    # 浏览次数
    view_count = models.IntegerField()
    # 创建时间
    create_time = models.DateTimeField()
    # 更新时间
    update_at = models.DateTimeField()
    # 是否公开.0否;1是
    isOpen = models.CharField(max_length=1, default="1")
    def __str__(self):
        return self.title
    class Meta:
        # 按创建时间倒序
        ordering = ['-create_time']

class NoteType(models.Model):
    """帖子类型(帖子所属模块)"""
    # 板块名称，unique是不能重复
    name = models.CharField(max_length=30,unique=True)
    # 模块管理员
    admin_user = models.ForeignKey('NoteUser',on_delete=models.CASCADE,)
    def __str__(self):
        return self.name

class NoteUser(models.Model):
    """ 用户表。继承django自带的用户认证系统 """
    # 用户
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    # 签名
    signature = models.CharField(max_length=100, default='这家伙没有签名')
    # 个人说明
    note = models.TextField()
    # 头像默认一个图片，upload_to会自动在根目录创建一个文件夹，支持上传
    photo = models.ImageField(upload_to=settings.UPLOAD_NOTEUSER_URL, default="static/upload/head_photo/default.jpg")
    def __str__(self):
        return self.user.username
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr),datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr),datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = str(getattr(self,attr))
        import json
        return json.dumps(d)

class IMG(models.Model):
    img = models.ImageField(upload_to=settings.UPLOAD_IMG_URL)
    # 名称
    name = models.CharField(max_length=20)
    # 类型.blog为新增时上传
    type = models.CharField(max_length=10)
    def __str__(self):
        return self.name

