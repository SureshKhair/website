from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def project(request):
    projects=Project.objects.all()
    context={'projects':projects}
    return render(request,'project/projects.html',context)

def projects(request,pk):
    projectobj=Project.objects.get(id=pk)
    return render(request,'project/single-project.html',{'project':projectobj})

def createproject(request):
    form=ProjectForm()

    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('project')

    context={'form':form}
    return render(request,'project/project_form.html',context)


def updateproject(request,pk):
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)

    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid:
            form.save()
            return redirect('project')

    context={'form':form}
    return render(request,'project/project_form.html',context)

def deleteproject(request,pk):
    project=Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project')
    context={'objects':project}
    return render(request,'project/delete_template.html',context)