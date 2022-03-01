from django.db import models
from django.forms import CharField

class User(models.Model):
    name = models.CharField(max_length=20)
    

# Create your models here.
class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField()

    