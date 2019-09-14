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
    #path('todo/by_id/<int:project_id>', views.todo_by_proj, name='show_todo_by_proj_old'),
    #path('todo_old/', views.todoitems, name='todoitems_old'),
    path('todo/add', views.form_add_todo, name='todoitem_add'),
    path('todo/delete/<int:todo_item_id>', views.form_delete_todoitem, name='todoitem_delete'),
    path('todo/', views.TodoitemsCBV.as_view(), name='todoitems'),
    path('todo/by_id/<int:project_id>', views.TodoitemsCBV.as_view(), name='show_todo_by_proj'),
]
