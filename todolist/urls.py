from django.urls import path, include

from . import views

app_name = 'todolist'

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('projects/add', views.form_add_project, name='add_project'),
    path('projects/delete/<int:project_id>', views.form_delete_project, name='delete_project'),
    path('todo/add', views.form_add_todo, name='todoitem_add'),
    path('todo/delete/<int:todo_item_id>', views.form_delete_todoitem, name='todoitem_delete'),
    path('todo/', views.TodoitemsListView.as_view(), name='todoitems'),
    path('todo/by_project/<int:project_id>', views.TodoitemsListView.as_view(), name='show_todo_by_proj'),
    path('todo/<pk>', views.TodoitemDetailView.as_view(), name='todoitem_detail'),
]
