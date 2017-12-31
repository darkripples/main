from django.contrib import admin
from blog import models

class Blog_admin(admin.ModelAdmin):
    # ����һ����������admin����ʾ��Ҫ��ʾ���ֶ�
    list_display = ('title','note_type','note','author','view_count','create_time','update_at')
    # ��һ��Ԫ�飬ĩβҪ�Ӷ���
    list_filter = ('create_time',)
    # ��admin�д��������������������ֶ�����'auther__user__username'��ʽ���˴�Ҫע�⡣
    search_fields = ('title','note','author__user__username')
    

admin.site.register(models.NoteContent, Blog_admin)
admin.site.register(models.NoteType)
admin.site.register(models.NoteUser)