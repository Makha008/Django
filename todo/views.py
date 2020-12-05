from django.shortcuts import get_object_or_404,render, HttpResponseRedirect

# Create your views here.

from django.http import HttpResponse
from .models import Task
from .forms import TaskForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    

def list(request):
    todo_items = Task.objects.all()
    return render(request, 'todo/index.html',{'all_items':todo_items})
    
def add_todo(request):
    
   new_item = Task(content=request.POST['content'])
   
   new_item.save()
   
   return HttpResponseRedirect('/todo/')
   
   
def delete_todo(request, todo_id):
    
   del_item = Task.objects.get(id=todo_id)
   
   del_item.delete()
   
   return HttpResponseRedirect('/todo/')
   
def update_task(request,todo_id):
    task = Task.objects.get(id=todo_id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/todo/')
    return render(request, "todo/edit.html", {"task_edit_form": form})
   
   
def Task_done(request,todo_id):
	task = Task.objects.get(id=todo_id)
	if request.method == 'POST':
		task.is_done = True
		task.save()
		return HttpResponseRedirect('/todo/')
