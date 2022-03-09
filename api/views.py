import os
import logging
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.conf import settings

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    """
    https://www.geeksforgeeks.org/django-upload-files-with-filesystemstorage/
    """

    if request.method == 'POST':
        request_file: File = request.FILES.get('document', None)

        if request_file:
            # https://docs.djangoproject.com/en/4.0/ref/files/storage/
            file_path = request_file.name
            fs = FileSystemStorage()
            logger.info('ファイルの保存を開始します')
            file = fs.save(file_path, request_file)
            logger.info('ファイルを保存しました : {0}'.format(file))

            saved_path = os.path.join(settings.MEDIA_ROOT, file_path)
            if os.path.exists(saved_path):
                file_size = os.path.getsize(saved_path)
                logger.info('{0} のファイルサイズは {1}バイト です'.format(saved_path, file_size))
            else:
                logger.error('{0} が保存されていません'.format(saved_path))
        else:
            logger.error('リクエストにファイルが見つかりませんでした')

    return render(request, 'index.html')
