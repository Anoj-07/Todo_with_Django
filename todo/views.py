from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
# Home view: shows task list and handles add

# View to handle displaying tasks and adding new ones
def home(request):
    if request.method == 'POST':
        new_task = request.POST.get('title')  # ✅ Correct: POST and 'title'
        if new_task:
            Task.objects.create(title=new_task)  # ✅ Save task
        return redirect('home')  # ✅ Prevent form resubmission on refresh

    tasks = Task.objects.all()  # ✅ Fetch all tasks from DB
    return render(request, 'todo/home.html', {'tasks': tasks})


#view to delete a task
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by its ID
    task.delete()
    return redirect('home')


# view to mark task completed
def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('home')