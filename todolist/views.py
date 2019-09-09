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

def doc_prefix_list(request):
    prefixes = models.DocPrefix.objects.all()
    prefixes_list = [(i.doc_prefix, i.doc_prefix_id) for i in prefixes]
    context = {'prefix_list': prefixes_list }
    return render(request, 'docmgr/docprefix.html', context)

def form_add_doc_prefix(request):
    form = forms.FormDocPrefix()

    if request.method == 'POST':
        form = forms.FormDocPrefix(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return doc_prefix_list(request)

    return render(request, 'docmgr/form_add_doc_prefix.html', {'form':form})

def form_delete_doc_prefix(request, doc_prefix_id):
    to_delete = get_object_or_404(models.DocPrefix, doc_prefix_id=doc_prefix_id)

    if request.method == 'POST':
        form = forms.FormDocPrefixDelete(request.POST)
        if form.is_valid():
            to_delete.delete()

    return doc_prefix_list(request)

def list_doc_revision(request, document_prefix):
    doc_prefix = get_object_or_404(models.DocPrefix, doc_prefix=document_prefix)
    documents = models.Document.objects.all().filter(doc_prefix_id=doc_prefix)
    revisions_list = [(i.revision, i.document_id) for i in documents]
    context = {'revisions_list': revisions_list, 'prefix': doc_prefix.doc_prefix }
    return render(request, 'docmgr/documents_list.html', context)

def form_add_doc_revision(request, document_prefix):
    form = forms.FormDocRevision()

    if request.method == 'POST':
        form = forms.FormDocRevision(request.POST)
        if form.is_valid():
            inst = form.save(commit=False)
            inst.doc_prefix_id = get_object_or_404(models.DocPrefix, doc_prefix=document_prefix)
            print(inst.doc_prefix_id)
            inst.save()
        return list_doc_revision(request, document_prefix)

    return render(request, 'docmgr/form_add_doc_revision.html', {'form':form, 'prefix':document_prefix})

def form_delete_doc_revision(request, document_id):
    to_delete = get_object_or_404(models.Document, document_id=document_id)

    if request.method == 'POST':
        form = forms.FormDocRevisionDelete(request.POST)
        if form.is_valid():
            to_delete.delete()

    return doc_prefix_list(request)


