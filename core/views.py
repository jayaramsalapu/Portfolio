from django.shortcuts import render
from .models import Profile
from skills.models import Skill
from projects.models import Project
from experience.models import Experience
from education.models import Education
from certificates.models import Certificate


def home(request):

    profile = Profile.objects.first()

    skills = Skill.objects.all()

    featured_projects = Project.objects.order_by('-featured', '-created_at')[:6]

    experiences = Experience.objects.all()[:3]

    educations = Education.objects.all()[:2]

    certificates = Certificate.objects.all()[:4]

    context = {
        "profile": profile,
        "skills": skills,
        "featured_projects": featured_projects,
        "experiences": experiences,
        "educations": educations,
        "certificates": certificates,
    }

    return render(request, "core/home.html", context)