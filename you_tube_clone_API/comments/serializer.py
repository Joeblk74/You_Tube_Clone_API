from rest_framework import serializers
from .models import Comment
from .models import Replies


class CommentSerializer(serializers.ModelSerialiser):
    class Meta:
        model= Comment
        fields = ['body', 'like', 'dislike', 'videoID']

class RepliesSerializer(serializers.ModelSerialiser):
    class Meta:
        model= Replies
        fields = ['body', 'commentID']