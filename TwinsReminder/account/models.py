from django.db import models
from django.conf import settings
import os

def file_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "attached_files")

class User_Notification(models.Model):
    category = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    #file = models.FilePathField("/files")
    instructor = models.CharField(max_length=50)
    student = models.CharField(max_length=50)
