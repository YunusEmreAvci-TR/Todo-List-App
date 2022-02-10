from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('completed/', views.completed, name='completed'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('todo_detail/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todo_completed/<int:id>', views.todo_completed, name='todo_completed'),
    path('todo_delete/<int:id>', views.todo_delete, name='todo_delete'),
    
]
