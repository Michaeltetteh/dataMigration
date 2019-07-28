from django.db import models


class Country(models.Model):
    name = models.TextField(max_length=50, blank=False, null=False)
    country_code = models.TextField(max_length=50, blank=True, null=True)
    time_zone = models.TextField(
        max_length=255, blank=True, null=True
    )

    def __str__(self):
        return self.name
