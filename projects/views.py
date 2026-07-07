

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    projects = Project.objects.all()

    context = {
        "projects": projects
    }

    return render(request, "projects/project_list.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    context = {
        "project": project
    }

    return render(request, "projects/project_detail.html", context)