from rest_framework.serializers import*
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import*

class PostSerializer(ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta():
        model = Comment
        fields = '__all__'

class RegisterSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def validate(self, attrs):
        username = attrs.get('username')
        if User.objects.filter(username = username).exists():
            raise ValidationError('user already exists')

        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(Serializer):
    username = CharField(max_length = 116)
    password = CharField(max_length = 116)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request = self.context.get('request'),
                username = username,
                password = password,
            )

            if user is None:
                raise ValidationError('user not found')

        attrs['user'] = user
        return attrs