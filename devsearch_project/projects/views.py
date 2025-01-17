from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm
# Create your views here.
def projects(request): 
    projects = Project.objects.all()
    return render(request,'projects/projects.html',{"projects":projects})



def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    context={'project':projectobj}
    return render(request,'projects/single_project.html',context)

def createProject(request):
    form=ProjectForm()
    if request.method =='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('projects')
    context={'form':form}
    return render(request,'projects/project-form.html',context)


def updateProject(request,pk):
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
        return redirect ('projects')
    context={'form': form}
    return render(request,'projects/project-form.html',context)


def deleteProject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context ={'object':project}
    return render(request,'projects/delete_template.html',context)



   
    



