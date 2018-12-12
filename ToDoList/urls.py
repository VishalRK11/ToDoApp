from django.urls import path
from ToDoList.views import *

app_name = 'ToDoList'

urlpatterns = [
    path('home/', home, name='home'),
    path('add/', add_task, name='add_task'),
    path('complete/<int:pk>', complete_task, name='complete_task'),
    path('delete-all/', delete_all, name='delete_all_tasks'),
    path('delete-completed/', delete_completed, name='delete_completed_tasks'),
]
