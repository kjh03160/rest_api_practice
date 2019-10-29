from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()

class Album(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images") # media/images 폴더에 업로드
    description = models.CharField(max_length=100)

class File(models.Model):
    author_name = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    file = models.FileField(blank=False, null=False, upload_to="files") # media/files 폴더에 업로드
    description = models.CharField(max_length=100)
    # 이미지 업로드 위해 pip install Pillow
