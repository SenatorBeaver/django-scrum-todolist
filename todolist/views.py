from django.forms import ModelForm, SelectDateWidget, SplitDateTimeWidget, DateTimeInput
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from todolist.forms import TodoitemForm
from . import models
from . import forms

# Create your views here.

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
    form_class = TodoitemForm
	
class TodoitemUpdateView(UpdateView):
    model = models.TodoItem
    form_class = TodoitemForm

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
            return models.TodoItem.objects.filter(done_date=None).filter(project=project)
        else:
            return models.TodoItem.objects.filter(done_date=None)

class TodoitemsToday(TodoitemsListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        tomorrow = timezone.datetime.today() + timezone.timedelta(days=1)
        return queryset.filter(due_date__lt=timezone.make_aware(tomorrow))

class TodoitemDetailView(DetailView):
    context_object_name = 'todoitem'
    model = models.TodoItem
    template_name = 'todolist/todoitem_detail.html'


def todoitem_done(request, pk):
    obj = get_object_or_404(models.TodoItem, pk=pk)
    obj.done_date = timezone.now()
    obj.save()
    #TODO redirect to previous viewed page
    return redirect('todolist:index')