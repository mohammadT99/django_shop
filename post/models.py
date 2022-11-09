from email.policy import default
from enum import unique
from secrets import choice
from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('P' , 'publish'),
        ('D','Draft'),
        
    )
    titel=models.CharField(max_length=200)
    slug=models.SlugField(max_length=100,unique=True)
    desc=models.TextField()
    image=models.ImageField(upload_to='image')
    publish=models.DateTimeField(default=timezone.now)
    crated=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHOICES)
    def __str__(self):
        return self.titel
    
    #<<<<----------------------------------------------------------------------->>>>>>>>
class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField( max_length=254)
    phone=models.CharField( max_length=11)
    masege=models.TextField()
    def __str__(self):
        return self.email



