from django.db import models


class Experience(models.Model):

    company = models.CharField(max_length=200)

    position = models.CharField(max_length=200)

    location = models.CharField(max_length=100)

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    currently_working = models.BooleanField(default=False)

    description = models.TextField()

    company_logo = models.ImageField(
        upload_to="experience/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-start_date"]

    def __str__(self):
        return f"{self.position} - {self.company}"