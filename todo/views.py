from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todos
from .forms import CreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    is_not_complated = Todos.objects.filter(is_complated = False)
    completed_count = len(Todos.objects.filter(is_complated = True))

    page = request.GET.get('page')
    results = 5
    paginator = Paginator(is_not_complated, results)

    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
    finally:
        todos = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
   
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return render(request, 'index.html', {
        'todos' : todos,
        'completed_count' : completed_count,
        'paginator' : paginator,
        'custom_range' : custom_range
    })

def completed(request):
    complated = Todos.objects.filter(is_complated = True)
    completed_count = len(Todos.objects.filter(is_complated = True))

    page = request.GET.get('page')
    results = 5
    paginator = Paginator(complated, results)

    try:
        todos = paginator.page(page)
    except PageNotAnInteger:
        page = 1
    except EmptyPage:
        page = paginator.num_pages
    finally:
        todos = paginator.page(page)

    leftIndex = (int(page) - 1)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 2)
   
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return render(request, 'completed.html', {
        'todos' : todos,
        'completed_count' : completed_count,
        'paginator' : paginator,
        'custom_range' : custom_range
    })

def todo_completed(request, id):
    todo = Todos.objects.filter(id = id)
    for t in todo:
        if t.is_complated == True:
            t.is_complated = False
            t.save()
            return redirect('completed')
        else:
            t.is_complated = True
            t.save()
            return redirect('index')

def todo_delete(request, id):
    todo = Todos.objects.filter(id = id).delete()
    return redirect(request.META.get('HTTP_REFERER'))

def create_todo(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            post = form.save(request.POST)
            post.save()
            return redirect('index')

    return render(request, 'create_todo.html')

def todo_detail(request, id):
    todo = Todos.objects.filter(id=id)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=todo[0])
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'todo_detail.html', {
        'todo' : todo[0],
    })