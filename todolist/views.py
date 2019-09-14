from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

from . import models
from . import forms

# Create your views here.

def index(request):
    return render(request, 'todolist/base.html')

def projects(request):
    projects = models.Project.objects.all()
    project_list = [(i.name, i.description, i.project_id) for i in projects]
    context = {'project_list': project_list }
    return render(request, 'todolist/projects.html', context)

def form_add_project(request):
    form = forms.FormProject()

    if request.method == 'POST':
        form = forms.FormProject(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return projects(request)

    return render(request, 'todolist/form_add_project.html', {'form':form})

def form_delete_project(request, project_id):
    to_delete = get_object_or_404(models.Project, project_id=project_id)

    if request.method == 'POST':
        form = forms.FormProjectDelete(request.POST)
        if form.is_valid():
            to_delete.delete()
    return projects(request)

def todo_by_proj(request, project_id):
    if project_id != None:
        project = get_object_or_404(models.Project, project_id=project_id)
    todo_objects = models.TodoItem.objects.all()
    todoitems_list = [(i.text, i.label_id, i.due_date, i.todo_item_id) for i in todo_objects]
    context = {'todo_list': todoitems_list }
    return render(request, 'todolist/todo.html', context)


def todoitems(request):
    return todo_by_proj(request, project_id=None)

class TodoitemsListView(ListView):
    template_name = 'todolist/todo.html'
    context_object_name = 'todo_list'
    model=models.TodoItem
    def get_queryset(self):
        if 'project_id' in self.kwargs:
            project = get_object_or_404(models.Project, project_id=self.kwargs['project_id'])
            return models.TodoItem.objects.filter(project=project)
        else:
            return models.TodoItem.objects.all()

class TodoitemDetailView(DetailView):
    context_object_name = 'todoitem_detail'
    model = models.TodoItem
    template_name = 'todolist/todoitem_detail.html'

def form_add_todo(request):
    form = forms.FormTodo()

    if request.method == 'POST':
        form = forms.FormTodo(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return todoitems(request)

    return render(request, 'todolist/form_add_todoitem.html', {'form':form})

def form_delete_todoitem(request, todo_item_id):
    to_delete = get_object_or_404(models.TodoItem, todo_item_id=todo_item_id)

    if request.method == 'POST':
        form = forms.FormTodoDelete(request.POST)
        if form.is_valid():
            to_delete.delete()
    return todoitems(request)

