from django.urls import path, include

from . import views

app_name = 'todolist'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.ProjectListView.as_view(), name='projects'),
    path('projects/<pk>', views.ProjectDetailView.as_view(), name='project_details'),
    path('projects/add', views.ProjectCreateView.as_view(), name='project_add'),
    path('projects/edit/<pk>', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/delete/<pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('todo/add', views.TodoitemCreateView.as_view(), name='todoitem_add'),
    path('todo/edit/<pk>', views.TodoitemUpdateView.as_view(), name='todoitem_edit'),
    path('todo/delete/<pk>', views.TodoitemDeleteView.as_view(), name='todoitem_delete'),
    path('todo/', views.TodoitemsListView.as_view(), name='todoitems'),
    path('todo/by_project/<int:project_id>', views.TodoitemsListView.as_view(), name='show_todo_by_proj'),
    path('todo/<pk>', views.TodoitemDetailView.as_view(), name='todoitem_detail'),
]
