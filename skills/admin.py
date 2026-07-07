from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "percentage",
        "order",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "order",
    )