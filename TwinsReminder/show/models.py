import os
from pyexpat import model
from unicodedata import category
from django.conf import settings
from django.db import models

def file_path():
    return os.path.join(settings.LOCAL_FILE_DIR, "attached_files")

class Notification(models.Model):
    category = models.CharField(max_length=50)
    date = models.DateTimeField('date published')
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    file = models.FilePathField(file_path)
    instructor = models.CharField(max_length=50)
    student = models.CharField(max_length=50)

# Create your models here.
