from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from . import models
from . import forms

# Create your views here.

def index(request):
    return render(request, 'todolist/base.html')

class ProjectListView(ListView):
    template_name = 'todolist/projects.html'
    context_object_name = 'projects'
    model=models.Project
    def get_queryset(self):
        return models.Project.objects.all()

class ProjectDetailView(DetailView):
    context_object_name = 'project_detail'
    model = models.Project
    template_name = 'todolist/project_details.html'

class ProjectCreateView(CreateView):
    model = models.Project
    fields = ('name', 'description', )

class ProjectUpdateView(CreateView):
    model = models.Project
    fields = ('name', 'description', )

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
        return HttpResponseRedirect(reverse('todolist:todoitems'))

    return render(request, 'todolist/form_add_todoitem.html', {'form':form})

def form_delete_todoitem(request, todo_item_id):
    to_delete = get_object_or_404(models.TodoItem, todo_item_id=todo_item_id)

    if request.method == 'POST':
        form = forms.FormTodoDelete(request.POST)
        if form.is_valid():
            to_delete.delete()
    return HttpResponseRedirect(reverse('todolist:todoitems'))

