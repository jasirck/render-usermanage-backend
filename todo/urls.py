from django.urls import path
from .views import todo_list_create_view, todo_retrieve_update_destroy_view

urlpatterns = [
    path('todos/', todo_list_create_view, name='todo-list-create'),
    path('todos/<int:pk>/', todo_retrieve_update_destroy_view, name='todo-retrieve-update-destroy'),
]
