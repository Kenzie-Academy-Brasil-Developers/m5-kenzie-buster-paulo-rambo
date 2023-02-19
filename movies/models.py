from django.db import models


class RatingChoices(models.TextChoices):
    A = "PG"
    B = "PG-13"
    C = "R"
    D = "NC-17"
    DEFAULT = "G"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.DEFAULT,
    )
    synopsis = models.TextField(null=True, default=None)
    owner = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )
