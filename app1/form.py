from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Comment

class CommentForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Thêm nhận xét của bạn...', 'rows': 10})
    )
    def __init__(self, *args, **kwargs):
        self.author = kwargs.pop('author',None)
        self.tutor = kwargs.pop('tutor',None)
        super().__init__(*args, **kwargs)
    def save(self, commit = True):
        comment = super().save(commit=False)
        comment.author = self.author
        comment.tutor = self.tutor
        comment.save()
    class Meta:
        model = Comment
        fields = ["body"]