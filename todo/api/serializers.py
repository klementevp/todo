from rest_framework import serializers

from main.models import Task, List 


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('user', 'task_name', 'due_date', 'comment', 'list')


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ('user', 'name', 'created_at')

