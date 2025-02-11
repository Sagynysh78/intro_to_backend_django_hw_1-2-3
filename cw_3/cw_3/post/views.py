from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница (перенаправление на /threads)
def home(request):
    return redirect('post:thread_list')

# Список всех Thread
def thread_list(request):
    threads = Thread.objects.all()
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:thread_list')
    else:
        form = ThreadForm()
    return render(request, 'threads/list.html', {'threads': threads, 'form': form})

# Детали Thread и связанных Post
def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = Post.objects.filter(thread=thread)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('post:thread_detail', thread_id=thread_id)
    else:
        form = PostForm()
    return render(request, 'threads/detail.html', {'thread': thread, 'posts': posts, 'form': form})

# Удаление Thread
def delete_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        thread.delete()
        return redirect('post:thread_list')
    return render(request, 'threads/delete_thread.html', {'thread': thread})

# Редактирование Thread
def edit_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('post:thread_detail', thread_id=thread_id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'threads/edit_thread.html', {'form': form, 'thread': thread})

# Удаление Post
def delete_post(request, thread_id, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post:thread_detail', thread_id=thread_id)
    return render(request, 'threads/delete_post.html', {'post': post})

# Редактирование Post
def edit_post(request, thread_id, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post:thread_detail', thread_id=thread_id)
    else:
        form = PostForm(instance=post)
    return render(request, 'threads/edit_post.html', {'form': form, 'post': post})