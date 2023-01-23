from django.urls import path

from api.views import TaskAPIView, TaskDetail, ListAPIView, ListDetailAPI

urlpatterns = [
    path('tasklist/', TaskAPIView.as_view()),
    path('task_detail/<int:pk>/', TaskDetail.as_view()),
    path('categorylist', ListAPIView.as_view()), 
    path('category_detail/<int:pk>/', ListDetailAPI.as_view())
]