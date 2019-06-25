from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm


def index_view(request):
    context = {}
    return render(request, "index.html", context)


def project_modify_view(request, project_id):
    obj = get_object_or_404(Project, hcsec_name=project_id)
    form = ProjectForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "ModifyProject.html", context)


def project_view(request):
    queryset = Project.objects.all() # list of objects

    context = {
        "object_list": queryset
    }
    return render(request, "Project.html", context)


def create_new_project_view(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        print("Form is valid")
        form.save()
        form = ProjectForm()

    context = {
        'form': form
    }
    return render(request, "CreateNew.html", context)
