from django.contrib import admin
from blog import models

class Blog_admin(admin.ModelAdmin):
    # 下面一行作用是在admin中显示需要显示的字段
    list_display = ('title','note_type','note','author','view_count','create_time','update_at')
    # 是一个元组，末尾要加逗号
    list_filter = ('create_time',)
    # 在admin中创建搜索，如果是外键的字段则用'auther__user__username'形式，此处要注意。
    search_fields = ('title','note','author__user__username')
    

admin.site.register(models.NoteContent, Blog_admin)
admin.site.register(models.NoteType)
admin.site.register(models.NoteUser)