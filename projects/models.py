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
    
    # Descriptions
    short_description = models.TextField(blank=True, default='')
    description = models.TextField(verbose_name="Full Description")  # Keeps original data
    
    # Detailed Documentation
    development_process = models.TextField(blank=True, default='')
    features = models.TextField(blank=True, default='')
    challenges = models.TextField(blank=True, default='')
    architecture = models.TextField(blank=True, default='')
    future_improvements = models.TextField(blank=True, default='')
    
    # Links
    thumbnail = models.ImageField(upload_to="projects/")
    github = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    documentation_url = models.URLField(blank=True, default='')
    
    # Settings
    featured = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=STATUS
    )
    display_order = models.IntegerField(default=0, help_text="Ordering display index (lower comes first)")
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('display_order', '-created_at')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

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