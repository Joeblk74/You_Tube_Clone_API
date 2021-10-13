from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=100)
    date = models.DateTimeField()
    user = models.CharField(max_length=25)
    like = models.BooleanField()
    dislike = models.BooleanField()

class Replies(models.Model):
    reply = models.CharField(max_length=100)
    date = models.DateTimeField()
    user = models.CharField(max_length=25)