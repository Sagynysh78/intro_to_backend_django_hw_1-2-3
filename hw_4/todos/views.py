from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo


def redirect_to_todo_lists(request):
    """Редирект с главной страницы на список ToDo-листов"""
    return redirect('todo_lists')


def todo_list_view(request):
    """Страница со списком всех ToDo-листов"""
    todo_lists = TodoList.objects.all()

    # Обработка создания нового списка
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        if title:
            TodoList.objects.create(title=title, description=description)
            return redirect("todo_lists")  # Перезагрузка списка

    return render(request, 'todo_lists.html', {'todo_lists': todo_lists})


def todo_list_detail(request, id):
    """Детальная страница ToDo-листа + задачи в нем"""
    todo_list = get_object_or_404(TodoList, id=id)
    todos = todo_list.todo_set.all()

    # Обработка добавления новой задачи
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        due_date = request.POST.get('due_date')
        status = 'status' in request.POST  # Чекбокс для статуса

        if title and due_date:  # Проверка, что поля заполнены
            Todo.objects.create(
                title=title,
                description=description,
                due_date=due_date,
                status=status,
                todo_list=todo_list
            )
            return redirect('todo_list_detail', id=id)  # Обновление страницы

    return render(request, 'todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})


def todo_list_delete(request, id):
    """Удаление ToDo-листа"""
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_lists')


def todo_list_edit(request, id):
    """Редактирование ToDo-листа"""
    todo_list = get_object_or_404(TodoList, id=id)

    if request.method == 'POST':
        todo_list.title = request.POST.get('title')
        todo_list.description = request.POST.get('description', '')
        todo_list.save()
        return redirect('todo_list_detail', id=id)

    return render(request, 'todo_list_edit.html', {'todo_list': todo_list})


def todo_delete(request, id):
    """Удаление задачи"""
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id  # Чтобы вернуться в тот же список
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)


def todo_edit(request, id):
    """Редактирование задачи"""
    todo = get_object_or_404(Todo, id=id)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description', '')
        todo.due_date = request.POST.get('due_date')
        todo.status = 'status' in request.POST  # Чекбокс статуса
        todo.save()
        return redirect('todo_list_detail', id=todo.todo_list.id)

    return render(request, 'todo_edit.html', {'todo': todo})
