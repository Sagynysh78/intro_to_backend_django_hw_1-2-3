# post/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Страница с постами
    path('', views.home, name='home'),  # Это будет отображать все посты на главной странице

    # API
    path('api/posts/', views.PostListView.as_view(), name='post-list'),  # Получение списка постов
    path('api/posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # Получение поста по ID
    path('api/posts/create/', views.PostCreateView.as_view(), name='post-create'),  # Создание поста
    path('api/posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Удаление поста
]
