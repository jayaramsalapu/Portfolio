from django.urls import path
from .views import experience_list

urlpatterns = [
    path("", experience_list, name="experience_list"),
]