from django.db import models
from app.models import User

class Content(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField(max_length=300)
    type = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content_id = models.ForeignKey(Content,on_delete=models.CASCADE)
