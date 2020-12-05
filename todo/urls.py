from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.list, name='list'),
    path('addTodo/', views.add_todo),
    path('delete/<int:todo_id>/',views.delete_todo,name='delete_todo'),
    path('update/<int:todo_id>/', views.update_task, name="update_task"),
    path('Task_done/<int:todo_id>/',views.Task_done, name="Task_done"),
    
    
]
