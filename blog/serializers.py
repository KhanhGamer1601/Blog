from rest_framework.serializers import*
from .models import*

class PostSerializer(ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'