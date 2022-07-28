from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_page.html', {'title': 'Задачник', 'tasks': tasks})

def create(request):
    error = ' '
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Неверная форма заполнения'
    form = TaskForm()
    dict = {
        'form': form
    }
    return render(request, 'tasks/create_page.html', dict)


