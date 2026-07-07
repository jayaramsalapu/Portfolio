from django.shortcuts import render
from .models import Certificate


def certificate_list(request):

    certificates = Certificate.objects.all()

    return render(
        request,
        "certificates/certificate_list.html",
        {
            "certificates": certificates
        }
    )