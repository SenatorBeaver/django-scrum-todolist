from django.forms import ModelForm, SelectDateWidget, SplitDateTimeWidget, DateTimeInput
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

class TodoitemForm(ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ('text', 'priority', 'due_date', 'project')
        widgets = {
            'due_date': DateTimeInput
        }

class TodoitemCreateView(CreateView):
    model = models.TodoItem
    form_class = TodoitemForm
	
class TodoitemUpdateView(TodoitemCreateView):
    pass

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
            return models.TodoItem.objects.filter(done=False).filter(project=project)
        else:
            return models.TodoItem.objects.filter(done=False)

class TodoitemsToday(TodoitemsListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        tomorrow = timezone.datetime.today() + timezone.timedelta(days=1)
        return queryset.filter(due_date__lt=timezone.make_aware(tomorrow))

class TodoitemDetailView(DetailView):
    context_object_name = 'todoitem'
    model = models.TodoItem
    template_name = 'todolist/todoitem_detail.html'

class TodoitemDone(TodoitemDetailView):
    model = models.TodoItem
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.done = True
        obj.save()
        return obj
