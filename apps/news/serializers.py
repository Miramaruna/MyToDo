from rest_framework import serializers
from django.contrib.auth.models import AbstractUser

from apps.news.models import ToDo, User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'user', 'is_completed', 'created_at', 'image']

from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, write_only=True)
    confirm_password = serializers.CharField(max_length=30, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'age', 'password', 'confirm_password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            age=validated_data['age']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')

        if password != confirm_password:
            raise serializers.ValidationError({'confirm_password': "Пароли не совпадают"})
        if len(password) < 8:
            raise serializers.ValidationError({'password': "Минимум 8 символов"})

        return attrs

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'age', 'created_at', 'email']

class DeleteToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'

class CreateToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'is_completed', 'user', 'image']

    def create(self, validated_data):
        todo = ToDo.objects.create(
            title = validated_data['title']
        )
        todo.save()
        return todo
    
    # def validate(self, attrs):
        
    #     return attrs