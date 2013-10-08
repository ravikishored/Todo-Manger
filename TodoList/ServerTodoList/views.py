from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import models
from django.template import Context, loader, RequestContext
import requests
import datetime
#from hello.settings import API
from  ServerTodoList.models import TodoList


def createTodo(request):
    
    if request.method == 'POST':
        todo = TodoList(title=request.POST['name'],description=request.POST['message'])
        todo.save()

    todoList = TodoList.objects.all()
    todoDic=dict()
    for todo in todoList:
        todoDic[todo.taskId]={'taskId':todo.taskId,'title':todo.title,'description':todo.description,'startdate':todo.startDate,'checked':todo.completed}
    data={'data':todoDic}
    return render_to_response("form.html",data,context_instance=RequestContext(request))
    
def done(request):
    if request.method == 'GET':
        todo = TodoList.objects.get(taskId=request.GET['todoid'])
        todo.completed='1'
        todo.endDate=datetime.datetime.now()
        todo.save()
    return createTodo(request)
    
