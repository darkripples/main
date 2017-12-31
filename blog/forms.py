# -*- coding: utf-8 -*-
from django.forms import ModelForm
from .models import NoteContent

class NoteContentForm(ModelForm):
    class Meta:
        model = NoteContent
        fields = '__all__'
        # 排除指定列
        exclude = ['note','author','view_count','create_time','update_at','note_type','isOpen']


