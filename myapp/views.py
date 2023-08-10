from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Project,Task
from .forms import CreateNewTask,CreateNewProject

def index_page(request):
    title=f"Welcome to my page!!!"
    return render(request,'index.html',{
        'title':title
    })


def about(request):
    return render(request,"about.html")

def projects(request):
    projects=list(Project.objects.values())
    return render(request,"project/projects.html",{
        'projects':projects
    })

def tasks(request):
    if request.method=="GET":
        tasks=Task.objects.all()
        return render(request,"tasks/tasks.html",{
        'tasks':tasks
        })


def task_delete(request,id):
    if request.method=="GET":
        tasks=Task.objects.all()
        return render(request,"tasks/tasks.html",{
        'tasks':tasks
        })
    task=Task.objects.get(id=id)
    task.delete()
    return redirect('tasks/')


def task_update(request,id):
    if request.method=="GET":
        tasks=Task.objects.all()
        return render(request,"tasks/tasks.html",{
        'tasks':tasks
        })
    if request.method=='POST':
        if 'done' in request.POST:
            task=Task.objects.filter(id=id)
            task.done=True
            task.update()
        tasks=Task.objects.all()
        return render(request, "tasks/tasks.html", {'tasks': tasks})



def create_task(request):
    if request.method=='GET':
        return render(request,"tasks/create_task.html",{
        'form':CreateNewTask()
    })
    if request.method == 'POST':    
        Task.objects.create(
        title=request.POST["title"],
        description=request.POST['description'],
        project_id=request.POST['project_id'])
        return redirect('/tasks')
    

def create_project(request):
    if request.method=='GET':
        return render(request,"project/create_project.html",{
            'form':CreateNewProject()
        })
    if request.method=='POST':
        Project.objects.create(
            name=request.POST['name']
        )
        return redirect("/projects")

def project_detail(request,id):
    if request.method=='GET':
        print(id)
        project=get_object_or_404(Project,id=id)
        task=Task.objects.filter(project_id=id)
        

        return render(request,"project/projects_detail.html",{
            'project':project,
            'tasks':task
        })
        