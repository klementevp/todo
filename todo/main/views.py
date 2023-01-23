from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from main.models import Task, List
from users.models import User
from main.forms import TaskUpdateForm, CreateListForm, CreateTaskForm


# Приветственная страница
def welcome(request):
    return render(request, 'main/welcome_page.html', context={})


# Отрисовка главное страницы с заданиями
@login_required(login_url='login')
def home(request, pk):
    user = User.objects.get(id=pk)
    lists = user.list_set.all()
    tasks = user.task_set.filter(is_done=False)
    paginator = Paginator(tasks, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'lists': lists,
        'tasks': tasks,
        'user': user,
        'page_obj': page_obj,
    }
    return render(request, 'main/home.html', context)


# Страница выполненных заданий
@login_required(login_url='login')
def finishedTasks(request, pk):
    user = User.objects.get(id=pk)
    tasks = user.task_set.filter(is_done=True)
    paginator = Paginator(tasks, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'tasks': tasks,
        'page_obj': page_obj,
    }
    return render(request, 'main/finished_tasks.html', context)


# Создание категории
@login_required(login_url='login')
def createList(request):
    form = CreateListForm()

    if request.method == 'POST':
        List.objects.create(
            user=request.user,
            name=request.POST.get('name')
        )
        return redirect('home_page', request.user.id)

    context = {
        'form': form,
    }
    return render(request, 'main/create_list.html', context)


# Создание задания
@login_required(login_url='login')
def createtask(request):
    form = CreateTaskForm()
    lists = List.objects.all()
    print(request.POST.get('list'))
    if request.method == 'POST':
        list_name_get = request.POST.get('list')
        list_name, created = List.objects.get_or_create(name=list_name_get, user_id=request.user.id)
        Task.objects.create(
            user=request.user,
            task_name=request.POST.get('task_name'),
            due_date=request.POST.get('due_date'),
            comment=request.POST.get('comment'),
            list=list_name,
        )
        return redirect('home_page', request.user.id)

    context = {
        'form': form,
        'lists': lists,
    }
    return render(request, 'main/create_task.html', context)


# Функция для установления метки is_done в True или False
@login_required(login_url='login')
def taskfinished(request, pk):
    user = User.objects.get(id=pk)
    task_id = request.GET.get('id', '')

    if task_id == '':
        return redirect('home_page', user.id)

    done = user.task_set.get(id=task_id)

    if not done.is_done:
        done.is_done = True
        done.save()
        return redirect('home_page', user.id)
    else:
        done.is_done = False
        done.save()
        return redirect('finished_page', user.id)

    return redirect(request, 'main/todofinished.html', context={})


# Обновить задание
@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    lists = List.objects.all()
    form = TaskUpdateForm(instance=task)

    if request.method == 'POST':
        list_name_get = request.POST.get('list')
        list_name, created = List.objects.get_or_create(name=list_name_get, user_id=request.user.id)
        task.list = list_name
        task.task_name = request.POST.get('task_name')
        task.due_date = request.POST.get('due_date')
        task.comment = request.POST.get('comment')
        task.save()
        return redirect('home_page', request.user.id)
    context = {
        'lists': lists,
        'form': form,
        'task': task,
    }
    return render(request, 'main/update_task.html', context)


@login_required(login_url='login')
def deletetask(request, pk):
    task = Task.objects.get(id=pk)
    lists = List.objects.all()

    context = {
        'lists': lists,
    }

    if request.method == 'POST':
        task.delete()
        return redirect('finished_page', request.user.id)
    return render(request, 'main/delete_task.html', context)
