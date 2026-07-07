from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "position",
        "company",
        "currently_working",
        "start_date",
    )

    list_filter = (
        "currently_working",
    )

    search_fields = (
        "company",
        "position",
    )