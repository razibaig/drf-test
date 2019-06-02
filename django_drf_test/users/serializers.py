from .models import NewUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('email', 'first_name', 'last_name', 'age', 'city', 'avatar', 'last_login',)


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = '__all__'

    def update(self, instance, validated_data):
        return super(CreateUserSerializer, self).update(instance, validated_data)
