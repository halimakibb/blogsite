from __future__ import unicode_literals

from django.db import models
from datetime import date
from time import time

def get_upload_file_name(instance, filename):
    return 'media/%s_%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.

class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    published = models.DateField(default = date.today, editable = False)
    updated = models.DateField(default = date.today, editable = False)
    likes = models.IntegerField(default=0, editable = False)
    thumbnail = models.FileField(upload_to=get_upload_file_name, default = None)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comments = models.TextField()