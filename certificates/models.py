from django.db import models


class Certificate(models.Model):

    title = models.CharField(max_length=200)

    organization = models.CharField(max_length=200)

    issue_date = models.DateField()

    credential_id = models.CharField(
        max_length=200,
        blank=True
    )

    certificate_image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True
    )

    certificate_file = models.FileField(
        upload_to="certificates/pdf/",
        blank=True,
        null=True
    )

    verification_url = models.URLField(blank=True)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-issue_date"]

    def __str__(self):
        return self.title