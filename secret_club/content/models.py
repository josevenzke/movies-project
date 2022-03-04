from django.db import models
from django.contrib.auth.models import User

class Content(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField(max_length=300)
    type = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    content = models.ForeignKey(Content,on_delete=models.CASCADE)

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.ForeignKey(Content,on_delete=models.CASCADE)
