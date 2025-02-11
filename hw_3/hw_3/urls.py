from django.contrib import admin
from django.urls import path, include
from post.views import home
from post import views

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('admin/', admin.site.urls),  # Админ-панель
    path('posts/', include('post.urls')),  # Подключаем URL-ы приложения post
]
