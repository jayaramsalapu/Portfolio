from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.

def project_list(request):
    projects = Project.objects.all()

    context = {
        "projects": projects
    }

    return render(request, "projects/project_list.html", context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)

    # Get all projects in the configured display order to find prev/next
    all_projects = list(Project.objects.all())
    
    prev_project = None
    next_project = None
    
    try:
        idx = all_projects.index(project)
        if idx > 0:
            prev_project = all_projects[idx - 1]
        if idx < len(all_projects) - 1:
            next_project = all_projects[idx + 1]
    except ValueError:
        pass

    # Fetch up to 3 related projects in the same category, excluding the current one
    related_qs = Project.objects.filter(category=project.category).exclude(id=project.id)
    related_projects = list(related_qs[:3])

    # If there are fewer than 3 related projects, pad with other projects
    if len(related_projects) < 3:
        needed = 3 - len(related_projects)
        already_included_ids = [project.id] + [p.id for p in related_projects]
        fallback_projects = Project.objects.exclude(id__in=already_included_ids)[:needed]
        related_projects.extend(list(fallback_projects))

    context = {
        "project": project,
        "prev_project": prev_project,
        "next_project": next_project,
        "related_projects": related_projects[:3],
    }

    return render(request, "projects/project_detail.html", context)