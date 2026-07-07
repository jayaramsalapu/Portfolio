from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Technology, Project, ProjectImage
from .widgets import CKEditorWidget

# Register your models here.

class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 3, 'cols': 80, 'placeholder': 'Enter a short summary for project cards...'}),
            'description': CKEditorWidget(),
            'development_process': CKEditorWidget(),
            'features': CKEditorWidget(),
            'challenges': CKEditorWidget(),
            'architecture': CKEditorWidget(),
            'future_improvements': CKEditorWidget(),
        }

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ("image_preview",)
    fields = ("image", "image_preview")
    
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 80px; border-radius: 4px; border: 1px solid #ddd;" />')
        return "No image uploaded yet"
    image_preview.short_description = "Preview"

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    
    list_display = (
        "title",
        "category",
        "featured",
        "display_order",
        "created_at",
    )

    list_filter = (
        "featured",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = ("technologies",)
    
    inlines = [
        ProjectImageInline
    ]

    readonly_fields = ("thumbnail_preview",)

    fieldsets = (
        ("Basic Information", {
            "fields": ("title", "slug", "category", "featured", "display_order"),
        }),
        ("Media Assets", {
            "fields": ("thumbnail", "thumbnail_preview"),
        }),
        ("External References", {
            "fields": ("github", "live_demo", "documentation_url"),
        }),
        ("Introduction", {
            "fields": ("short_description",),
        }),
        ("Detailed Documentation (Collapsible)", {
            "classes": ("collapse",),
            "fields": (
                "description",
                "development_process",
                "features",
                "challenges",
                "architecture",
                "future_improvements",
            ),
        }),
        ("Technologies Stack", {
            "fields": ("technologies",),
        }),
    )

    def thumbnail_preview(self, obj):
        if obj.thumbnail:
            return mark_safe(f'<img src="{obj.thumbnail.url}" style="max-height: 180px; border-radius: 8px; border: 1px solid #ccc; box-shadow: 0 2px 4px rgba(0,0,0,0.1);" />')
        return "No thumbnail uploaded yet"
    thumbnail_preview.short_description = "Thumbnail Preview"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    prepopulated_fields = {
        "slug": ("name",)
    }

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    ordering = ("name",)