import sys
from .models import Post
from users.models import NewUser
from rest_framework import serializers
sys.path.append("..")


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=NewUser.objects.all())

    class Meta:
        model = Post
        fields = '__all__'
