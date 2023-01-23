from django.db import models
from users.models import User


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=65, verbose_name='Категория')
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    task_name = models.CharField(max_length=255, verbose_name='Задание')
    due_date = models.DateField(verbose_name='Дата выполнения')
    comment = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категория')
    is_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['-created_at']

    def __str__(self):
        return self.task_name

