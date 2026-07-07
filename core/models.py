from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=150)

    profile_image = models.ImageField(upload_to="profile/")
    cover_image = models.ImageField(upload_to="cover/", blank=True, null=True)

    bio = models.TextField()

    email = models.EmailField()
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    resume = models.FileField(upload_to="resume/", blank=True, null=True)

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name