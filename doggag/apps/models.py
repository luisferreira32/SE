from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    #will have an image here
