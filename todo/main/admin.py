from django.contrib import admin
from main.models import *


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('name', 'created at')
    prepopulated_fields = {'slug': ('name', 'user')}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'task_name', 'created_at', 'is_done')
    list_filter = ('created_at', 'user')
    search_fields = ('user', 'created_at', 'task_name')



