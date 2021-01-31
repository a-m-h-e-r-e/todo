from django.urls import path

from . import views

app_name = 'todo_app'

urlpatterns = [
	path('', views.index, name='index'),
	path('add_task/', views.add_task, name='add_task'),
	path('mark_task_complete/', views.mark_task_complete, name='mark_task_complete'),
	path('unmark_task_complete/', views.unmark_task_complete, name='unmark_task_complete'), 
	path('delete_task/', views.delete_task, name='delete_task'),
	path('update_task/', views.update_task, name='update_task')
]