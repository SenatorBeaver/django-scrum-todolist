from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class ProjectUpdateView(UpdateView):
    model = models.Project
    fields = ('name', 'description', )

class ProjectDeleteView(DeleteView):
    model = models.Project
    success_url = reverse_lazy('todolist:projects')

class TodoitemCreateView(CreateView):
    model = models.TodoItem
    fields = ('text', 'priority', 'due_date', 'project')

class TodoitemUpdateView(UpdateView):
    model = models.TodoItem
    fields = ('text', 'priority', 'due_date')

class TodoitemDeleteView(DeleteView):
    model = models.TodoItem
    success_url = reverse_lazy('todolist:todoitems')


class TodoitemsListView(ListView):
    template_name = 'todolist/todoitem.html'
    context_object_name = 'todo_list'
    model=models.TodoItem
    def get_queryset(self):
        if 'id' in self.kwargs:
            project = get_object_or_404(models.Project, id=self.kwargs['id'])
            return models.TodoItem.objects.filter(project=project)
        else:
            return models.TodoItem.objects.all()

class TodoitemDetailView(DetailView):
    context_object_name = 'todoitem'
    model = models.TodoItem
    template_name = 'todolist/todoitem_detail.html'

