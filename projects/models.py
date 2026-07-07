from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Project(models.Model):

    STATUS = (
        ("Completed","Completed"),
        ("Ongoing","Ongoing"),
    )

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    technologies = models.ManyToManyField(Technology)

    description = models.TextField()

    thumbnail = models.ImageField(upload_to="projects/")

    github = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.title 

class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to="projects/gallery/")

    def __str__(self):
        return self.project.title