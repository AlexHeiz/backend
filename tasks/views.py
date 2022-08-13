from django.shortcuts import render, redirect, reverse
from .models import Task
from .forms import TaskForm


def tasks(request):
    post_pk = request.POST.get('DeleteButton')
    if post_pk:
        Task.objects.filter(pk=post_pk).delete()

    tasks = Task.objects.order_by('-created_date')
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