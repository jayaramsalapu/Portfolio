from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "organization",
        "issue_date",
    )

    search_fields = (
        "title",
        "organization",
    )

    ordering = (
        "-issue_date",
    )