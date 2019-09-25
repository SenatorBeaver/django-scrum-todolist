from django.urls import path, include

from . import views

app_name = 'todolist'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.TodoitemsToday.as_view(), name='index'),
    path('refresh/', views.refresh_task, name='refresh'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('projects/add', views.ProjectCreateView.as_view(), name='project_add'),
    path('projects/<pk>', views.ProjectDetailView.as_view(), name='project_details'),
    path('projects/edit/<pk>', views.ProjectUpdateView.as_view(), name='project_edit'),
    path('projects/delete/<pk>', views.ProjectDeleteView.as_view(), name='project_delete'),
    path('todo/', views.TodoitemsListView.as_view(), name='todoitems'),
    path('todo/add', views.TodoitemCreateView.as_view(), name='todoitem_add'),
    path('todo/edit/<pk>', views.TodoitemUpdateView.as_view(), name='todoitem_edit'),
    path('todo/edit/time/<pk>', views.TodoitemUpdateTimeView.as_view(), name='todoitem_time_edit'),
    path('todo/delete/<pk>', views.TodoitemDeleteView.as_view(), name='todoitem_delete'),
    path('todo/details/<pk>', views.TodoitemDetailView.as_view(), name='todoitem_detail'),
    path('todo/done/<pk>', views.todoitem_done, name='todoitem_done'),
    path('todo/by_project/<int:id>', views.TodoitemsListView.as_view(), name='show_todo_by_proj'),
]
