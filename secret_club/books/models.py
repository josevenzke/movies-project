from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField(max_length=300)


    
