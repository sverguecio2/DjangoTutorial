from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = "Curso de Django"
    return render(request, 'index.html', {'title': title})  # Agrego el título


def hello(request, username):
    print(username)
    return HttpResponse("Hello!" + str(username))


def about(request):
    return render(request, 'about/about.html')


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def tasks(request):
    # tasks = get_object_or_404(Task, id=id)
    # print(tasks)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'GET':
        print(request.GET)
        # Agrego el formulario
        return render(request, 'tasks/create_task.html', {'form': CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        print(request.GET)
        # Agrego el formulario
        return render(request, 'projects/create_project.html', {'form': CreateNewProject()})
    else:
        Project.objects.create(
            name=request.POST['name']) # Creo el proyecto
        return redirect('/projects/') # Redirijo a la vista projects
