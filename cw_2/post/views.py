from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .forms import PostForm


# Главная страница, отображающая посты и форму для добавления нового поста
def home(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перезагружаем страницу после добавления
    else:
        form = PostForm()

    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts, 'form': form})


# API для получения списка постов и их создания
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# API для получения одного поста по ID
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# API для создания поста
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# API для удаления поста
class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
