from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import*
from .models import*
from .serializers import*

# Create your views here.
class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated,]