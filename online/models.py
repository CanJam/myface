#!-*-coding:UTF-8-*-
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.username
# Create your models here.
