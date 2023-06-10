from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from . import serializers

from rest_framework.permissions import IsAuthenticated

from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework import generics


@api_view(['GET'])
def apiRoutes(request):
	api_urls = {
		'List':'/task-list/',
		'Create':'/task-create/',
		'Read Update Delete':'/task-detail/<str:pk>/',
		'Token':'/api/token/',
		'Token Refresh':'/api/token/refresh/',

		}

	return Response(api_urls)



class TaskCreate(generics.CreateAPIView):
	permission_classes = (IsAuthenticated,)
	serializer_class = TaskSerializer
	queryset = Task.objects.all()


class TaskList(generics.ListCreateAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Task.objects.all()
	serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthenticated,)
	queryset = Task.objects.all()
	serializer_class = TaskSerializer