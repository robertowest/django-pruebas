from django.db import models

from ckeditor.fields import RichTextField 
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    content = RichTextField(blank=True, null=True) 
    content2 = RichTextUploadingField(blank=True, null=True, config_name='special')
