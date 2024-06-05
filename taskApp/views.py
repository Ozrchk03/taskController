from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegisterForm, ProjectForm, TaskForm
from .models import Project, Task, Profile


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('projects')
        else:
            return render(request, 'authorize.html', {'error': 'Invalid login'})
    return render(request, 'authorize.html')


def logout(request):
    auth_logout(request)
    return redirect('login')

def home(request):
    if request.user.is_authenticated:
        return redirect('projects')
    else:
        return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматичний вхід після реєстрації
            return redirect('projects')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})



def project_list(request):
    if not request.user.is_authenticated:
        return redirect('login')
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form})


def task_list(request, project_id):
    if not request.user.is_authenticated:
        return redirect('login')
    tasks = Task.objects.filter(project_id=project_id)
    return render(request, 'tasks.html', {'tasks': tasks})


def profile(request, user_id):
    if not request.user.is_authenticated:
        return redirect('login')
    profile = Profile.objects.get(user_id=user_id)
    return render(request, 'profile.html', {'profile': profile})


def personnel(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Assuming a model for personnel
    personnel = User.objects.filter(is_staff=True)  # Assuming staff are personnel
    return render(request, 'personnel.html', {'personnel': personnel})
