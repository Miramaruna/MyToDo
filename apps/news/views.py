
# from rest_framework import mixins, viewsets
# from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from apps.news.models import User, ToDo
from apps.news.serializers import UserRegisterSerializer, UserSerializers, ToDoSerializer, CreateToDoSerializers
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.conf import settings
from apps.news.forms import CustomAuthenticationForm

class Pagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10

class DeleteAllToDoApiView(ListAPIView):
    queryset = ToDo.objects.all()
    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        otvet = ToDo.objects.all().delete()
        return otvet({"message": "Все записи удалены их вообще нету пон?"}, status=204)

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    pagination_class = Pagination
    permission_classes = [IsAuthenticated,]

class TodoCreateApiView(CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = CreateToDoSerializers
    permission_classes = [IsAuthenticated,]

class ToDoApiView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated,]
    pagination_class = Pagination

def main(request):
    todos = ToDo.objects.all()
    return render(request, 'home.html', {'todos': todos})

@login_required
def todohome(request):
    # Получить список To-Do для текущего пользователя
    todos = ToDo.objects.filter(user=request.user)[:15]
    if request.method == 'POST' and 'title' in request.POST:
        # Добавление новой задачи
        title = request.POST.get('title')
        if title:
            # Создать задачу и связать её с текущим пользователем
            ToDo.objects.create(user=request.user, title=title)
            return redirect('todo')  # Перенаправление на ту же страницу
    return render(request, 'todo.html', {'todos': todos})

def mark_completed(request, todo_id):
    # Получаем задачу из базы данных
    todo = get_object_or_404(ToDo, id=todo_id)
    todo.is_completed = True
    todo.save()
    return redirect('todo')

def delete_todo(request, todo_id):
    # Удаление задачи
    todo = get_object_or_404(ToDo, id=todo_id)
    todo.delete()
    return redirect('todo')

def register(request):
    if request.method == "POST":
        form = UserRegisterSerializer(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Регистрация прошла успешно!")
            # После регистрации, направляем на страницу todo
            return redirect('/todo/')  # Убедитесь, что здесь правильный путь
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserRegisterSerializer()

    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # Проверяем значение чекбокса
        
        # Попытка аутентификации пользователя
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Вход пользователя
            login(request, user)
            
            if remember_me:
                # Устанавливаем время жизни сессии по умолчанию (например, 30 дней)
                request.session.set_expiry(60 * 60 * 24 * 30)  # 30 дней
            else:
                # Устанавливаем сессию до закрытия браузера
                request.session.set_expiry(0)
            
            messages.success(request, "Вы успешно вошли!")
            return redirect('todo')  # Перенаправление на страницу "To Do list"
        else:
            # Если аутентификация не удалась
            messages.error(request, "Неверное имя пользователя или пароль")
    
    return render(request, 'login.html')


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm

    def form_valid(self, form):
        response = super().form_valid(form)
        # Если "Запомнить меня" не выбрано, установим куку для сессии
        if not form.cleaned_data.get('remember_me'):
            self.request.session.set_expiry(0)  # Сессия закончится при закрытии браузера
        else:
            # Сессия будет длиться (например) 2 недели
            self.request.session.set_expiry(settings.SESSION_COOKIE_AGE)
        return response
