from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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

