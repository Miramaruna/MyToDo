from django.urls import path
from apps.news.views import main, mark_completed, delete_todo, register, todohome, login_view
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', main, name='home'),  # Главная страница
    path('todo/', login_required(todohome), name='todo'),
    path('mark_completed/<int:todo_id>/', mark_completed, name='mark_completed'),
    path('delete_todo/<int:todo_id>/', delete_todo, name='delete_todo'), 
    path("register/", register, name="register"),
    path('login/', login_view, name="login"),
]