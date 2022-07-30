from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView

from rest_framework import generics
from .serializers import TaskSerializer


def tasks(request):

    print('*'*60)
    print('GET params')
    print(request.GET)
    print('')
    print('POST params')
    print(request.POST)
    print('*' * 60)

    print('YO')

    post_pk = request.POST.get('DeleteButton')
    if post_pk:
        print('post_pk:', post_pk)
        print('Task.objects.filter(pk=post_pk)', Task.objects.filter(pk=post_pk))
        Task.objects.filter(pk=post_pk).delete()
        if Task.objects.filter(pk=post_pk).exists():
            Task.objects.get(pk=post_pk).delete()

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









