from django.urls import path, include

from . import views

app_name = 'docmgr'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('projects/add', views.form_add_project, name='add_project'),
    path('projects/delete/<int:project_id>', views.form_delete_project, name='delete_project'),
    path('doc_prefix', views.doc_prefix_list, name='doc_prefix'),
    path('doc_prefix/add', views.form_add_doc_prefix, name='add_doc_prefix'),
    path('doc_prefix/delete/<int:doc_prefix_id>', views.form_delete_doc_prefix, name='delete_doc_prefix'),
    path('documents/<str:document_prefix>/list', views.list_doc_revision, name='list_doc_revision'),
    path('documents/<str:document_prefix>/add', views.form_add_doc_revision, name='add_doc_revision'),
    path('documents/<int:document_id>/delete', views.form_delete_doc_revision, name='delete_doc_revision'),
]
