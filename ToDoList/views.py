from django.shortcuts import render, redirect

from ToDoList.models import Todo
from ToDoList.forms import TodoForm


def home(request):
    to_do_list = Todo.objects.values().order_by('id')
    form = TodoForm
    context = {
        'text': to_do_list,
        'form': form,
    }
    return render(request=request, template_name='ToDoList/home.html', context=context)


def add_task(request):
    pass


def complete_task(request):
    todo = Todo.objects.get(pk=id)
    todo.complete = True
    todo.save()
    return redirect('ToDoList:home')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('ToDoList:home')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('ToDoList:home')
