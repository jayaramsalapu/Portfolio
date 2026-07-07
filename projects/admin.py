

# Register your models here.
from django.contrib import admin
from .models import (
    Category,
    Technology,
    Project,
    ProjectImage,
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "status",
    )

    list_filter = (
        "featured",
        "status",
        "category",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    inlines = [
        ProjectImageInline
    ]


admin.site.register(Category)

admin.site.register(Technology)