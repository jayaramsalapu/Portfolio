from django.urls import path
from .views import education_list

urlpatterns = [
    path("", education_list, name="education_list"),
]