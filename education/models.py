from django.db import models


class Education(models.Model):

    # Degree Name
    degree = models.CharField(max_length=200)

    # College / University Name
    college = models.CharField(max_length=200)

    # Branch / Stream
    field_of_study = models.CharField(max_length=200)

    # College Location
    location = models.CharField(max_length=100)

    # Course Start Date
    start_date = models.DateField()

    # Course End Date
    end_date = models.DateField()

    # CGPA or Percentage
    cgpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        blank=True,
        null=True
    )

    # Short Description
    description = models.TextField(
        blank=True,
        null=True
    )

    # Display Order
    order = models.PositiveIntegerField(default=0)

    # Created Time
    created_at = models.DateTimeField(auto_now_add=True)

    # Updated Time
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-start_date"]
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.college}"