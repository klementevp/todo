from django.urls import path
from main.views import *

urlpatterns = [
    path('', welcome, name='welcome_page'),
    path('home/<int:pk>', home, name='home_page'),
    path('finished_tasks/<int:pk>', finishedTasks, name='finished_page'),

    path('create_list/', createList, name='create_list'),
    path('create_task/', createtask, name='create_task'),
    path('delete_task/<int:pk>', deletetask, name='delete_task'),

    path(r'todofinish/<int:pk>', taskfinished, name='task_finished'),
    path('update_task/<int:pk>', updateTask, name='update_task'),
]