from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django import forms
# from django.contrib.auth.forms import AuthenticationForm

# Create your models here.

class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        verbose_name='Имя пользователя',
        unique=True
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    created_at = models.DateField(
        verbose_name='Дата создания пользователя',
        auto_now_add=True
    )
    age = models.IntegerField(
        verbose_name='Возраст пользователя',
        null=True,
        blank=True  
    )
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Пользователи'

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

    title = models.CharField(
        verbose_name='Заголовок',
        max_length=50
    )
    description = models.TextField(
        verbose_name='описание'
        )
    is_completed = models.BooleanField(
        verbose_name='Выполнено',
        null=True,
        blank=True 
    )
    created_at = models.DateField(
        verbose_name='Дата создания задачи',
        auto_now_add=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Задачи"
    