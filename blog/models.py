from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from datetime import date
from time import time

def get_upload_file_name(instance, filename):
    return 'media/%s_%s' % (str(time()).replace('.', '_'), filename)

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, email, name, password, **kwargs):
        user = self.model(
                          email = self.normalize_email(email),
                          name = name,
                          is_active = True,
                          **kwargs
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, name, password, **kwargs):
        user = self.model(
                          email = self.normalize_email(email),
                          name = name,
                          is_staff = True,
                          is_superuser = True,
                          is_active = True,
                          **kwargs
        )
        user.set_password(password)
        user.save()
        return user        

class User(AbstractBaseUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 20, unique = True)
    is_active = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name
    
    objects = UserManager()
    
class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    published = models.DateField(default = date.today, editable = False)
    updated = models.DateField(default = date.today, editable = False)
    likes = models.IntegerField(default=0, editable = False)
    author = models.ForeignKey(User, default = '', editable = False)
    thumbnail = models.FileField(upload_to=get_upload_file_name, default = None)
    def __unicode__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article)
    comments = models.TextField()