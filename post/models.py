from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200,default='')
    post = models.TextField()
    author = models.ForeignKey('auth.User', related_name='post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)