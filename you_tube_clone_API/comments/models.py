from django.db import models

# Create your models here.
class Comment(models.Model):
    body = models.TextField(max_length=250, null=True)
    like = models.IntegerField()
    dislike = models.IntegerField()
    videoID = models.TextField(max_length=50, null=True)
    

class Replies(models.Model):
    body = models.TextField(max_length=250, null=True)
    commentID = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)