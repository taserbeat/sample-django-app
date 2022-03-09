from django.db import models

# Create your models here.


class UploadedFile(models.Model):
    """
    アップロードされるファイルのモデル
    """

    file = models.FileField(upload_to='file')
