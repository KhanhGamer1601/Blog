from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import*
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
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

class GetCommentView(APIView):
    def get(self, request, user_id):
        comment = Comment.objects.all().filter(user = user_id)
        serializer = CommentSerializer(comment, many = True)
        return Response(serializer.data)

class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user = user)
            response = Response()
            response.set_cookie(key = 'key', value = token.key, httponly = True, secure = True, samesite = 'strict')
            response.data = {
                'key': token.key
            }
            return response