from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404	
from .models import Todos
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def index(request):
	task_list = Todos.objects.all()
	output = ', '.join([q.task for q in task_list])
	context = {
		'task_list': task_list
	}
	return render(request, 'todo_app/index.html', context)

def add_task(request):
	new_task = request.GET.get('input_task')
	todo = Todos(task=new_task)
	todo.save()
	return HttpResponseRedirect(reverse('todo_app:index'))

def mark_task_complete(request):
	id = request.GET.get('id')
	try:
		todo = Todos.objects.get(pk=id)
	except Todos.DoesNotExist:
		raise Http404("Todo does not exist")
	todo.completed = True
	todo.save()
	return HttpResponseRedirect(reverse('todo_app:index'))

def unmark_task_complete(request):
	id = request.GET.get('id')
	try:
		todo = Todos.objects.get(pk=id)
	except Todos.DoesNotExist:
		raise Http404("Todo does not exist")
	todo.completed = False
	todo.save()
	return HttpResponseRedirect(reverse('todo_app:index'))

def delete_task(request):
	id = request.GET.get('id')
	try:
		todo = Todos.objects.get(pk=id)
	except Todos.DoesNotExist:
		raise Http404("Todo does not exist")
	todo.delete()
	return HttpResponseRedirect(reverse('todo_app:index'))

def update_task(request):
	id = request.GET.get('id')
	updated_task = request.GET.get('updated_task')
	try:
		todo = Todos.objects.get(pk=id)
	except Todos.DoesNotExist:
		raise Http404("Todo does not exist")
	todo.task = updated_task
	todo.save()
	return HttpResponseRedirect(reverse('todo_app:index'))
	