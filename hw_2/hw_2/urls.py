from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movie.urls')),  # добавляем URL для movies
    path('articles/', include('blog.urls')),  # добавляем URL для articles
]
