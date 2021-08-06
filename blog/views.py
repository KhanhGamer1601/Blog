from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import*
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import*
from .serializers import*

# Create your views here.
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]

class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated,]

class GetCommentView():
    def get(self, request, user_id):
        comment = Comment.objects.all().filter(user = user_id)
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)