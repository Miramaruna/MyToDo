from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.news.views import UserApiView, UserCreateAPIView, DeleteAllToDoApiView, TodoCreateApiView, ToDoApiView
# from .serializers import StudentTransaktionCreateApiView

router = DefaultRouter()
# router.register("s_viewsets", RecipeViewsSets, basename='api-recipe')

urlpatterns = [
    path('users/', UserApiView.as_view(), name='users'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('todo/delete/all', DeleteAllToDoApiView.as_view(), name='delete_todo_all'),
    path('todo/create', TodoCreateApiView.as_view(), name='create_todo'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('todo/', ToDoApiView.as_view(), name='ToDo')
]

# urlpatterns += router.urls