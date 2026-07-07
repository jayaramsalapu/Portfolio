from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):

    list_display = (
        "degree",
        "college",
        "start_date",
        "end_date",
    )

    search_fields = (
        "degree",
        "college",
    )

    ordering = (
        "-start_date",
    )