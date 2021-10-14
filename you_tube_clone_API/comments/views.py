from django.shortcuts import render
from .models import Comment
from .models import Replies
from .serializer import CommentSerializer
from .serializer import RepliesSerializer
from rest_Framework.views import APIView
from rest_Framework.response import Response
from rest_Framework import status


# Create your views here.
class VideoComments (APIView):

    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer (comments, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Replies (APIView):
    
    def get(self, request):
        replies = Replies.objects.all()
        serializer = RepliesSerializer (replies, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = RepliesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)