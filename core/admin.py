from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name", "profession", "email", "phone", "location")
    search_fields = ("name", "profession", "email", "phone", "location")
    list_filter = ("created_at", "updated_at")