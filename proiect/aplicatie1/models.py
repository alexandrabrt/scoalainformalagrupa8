from django.db import models


class Location(models.Model):

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.city} - {self.country}"
