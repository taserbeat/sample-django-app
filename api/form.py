# https://blog.janjan.net/2021/02/17/python-django-file-upload-setup/

from django import forms
from .models import UploadedFile


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ('file',)
