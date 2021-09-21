from django.urls import path
from . import views

urlpatterns = [
    path('', views.Todolist, name='todo-list'),
    path('create', views.TodoForm, name='todo-form'),
    path('delete', views.Delete, name='delete'),
    path('update', views.Update, name='update'),
    path('search', views.search, name='search'),
]