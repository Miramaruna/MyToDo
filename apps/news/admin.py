from django.contrib import admin
from apps.news.models import ToDo, User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'age']
    list_filter = ['id', 'username', 'age']
    search_fields = ['id', 'username', 'age']
    # list_editable = ['is_active', ]

@admin.register(ToDo)
class ToDonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'created_at', 'is_completed']
    list_filter = ['id', 'title', 'description', 'created_at', 'is_completed']
    search_fields = ['id', 'title', 'description', 'created_at', 'is_completed']