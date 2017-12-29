from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import Context, loader, Template
from django.http import HttpResponse,HttpResponseRedirect

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer

from .models import task
from .serializers import taskSerializer
import json

#list all tasks or create a new
# tasks/
class tasklist(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'homepage.html'
	def get(self, request):
		toDoTasks=task.objects.filter(isDone=False).order_by('-taskid')
		doneTasks=task.objects.filter(isDone=True).order_by('-taskid')
		return Response({'toDoTasks':toDoTasks,'doneTasks':doneTasks})

	def post(self,request,format=None):
		serializer = taskSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return HttpResponseRedirect('/')
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteTask(request,taskid):
	task.objects.filter(taskid=taskid).delete()
	return HttpResponseRedirect('/')

def doneTask(request,taskid):
	task.objects.filter(taskid=taskid).update(isDone=True)
	return HttpResponseRedirect('/')

def undoneTask(request,taskid):
	task.objects.filter(taskid=taskid).update(isDone=False)
	return HttpResponseRedirect('/')
