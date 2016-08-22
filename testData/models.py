from django.db import models
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 500)
    team = models.CharField(max_length =250)
    persona = models.CharField(max_length =250)
    created_date = models.DateTimeField(default = timezone.now)
    sourceURL = models.CharField(max_length= 250)

def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
    
