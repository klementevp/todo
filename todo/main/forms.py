from django.forms import ModelForm

from main.models import Task, List


class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'is_done']


class CreateListForm(ModelForm):
    class Meta:
        model = List
        fields = ['name', ]


class CreateTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['user', 'created_at', 'is_done']

