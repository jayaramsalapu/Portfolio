from django.db import models


class Skill(models.Model):

    CATEGORY_CHOICES = (
        ("Frontend", "Frontend"),
        ("Backend", "Backend"),
        ("Database", "Database"),
        ("DevOps", "DevOps"),
        ("Tools", "Tools"),
    )

    name = models.CharField(max_length=100)

    percentage = models.PositiveIntegerField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: fa-python"
    )

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name