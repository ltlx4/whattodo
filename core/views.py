from urllib.request import Request
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Todo


# Create your views here.
def index(request):
    todos = Todo.objects.all().order_by('-id')
    context = {
        'todos':todos,
    }
    return render(request, 'core/index.html', context)

@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')

    if title:
        Todo.objects.create(task=title)
    
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'partials/todos.html', {'todos': todos})

@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'partials/todos.html', {'todos': todos})

@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()

    todos = Todo.objects.all().order_by('-id')
    return render(request, 'partials/todos.html', {'todos': todos})

    