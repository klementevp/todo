from django.http import Http404
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView 

from api.serializers import TaskSerializer, ListSerializer
from main.models import Task, List


# Представление для заданий
class TaskAPIView(APIView):

    def get(self, request):
        t = Task.objects.all()

        return Response({'tasks': TaskSerializer(t, many=True).data})

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Представление для категорий
class ListAPIView(APIView):

    def get(self, request):
        lists = List.objects.all()
        serializer = ListSerializer(lists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API для работы с конкретным заданием
class TaskDetail(APIView):
    def get_object(self, pk, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        try:
            instance = Task.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        serializer = TaskSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'task': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListDetailAPI(APIView):
    def get_object(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        try:
            list = List.objects.get(pk=pk)
        except List.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        list = List.objects.get(pk=pk)
        serializer = ListSerializer(list)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        try:
            instance = List.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        serializer = ListSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        list = List.objects.get(pk=pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




