from django.db import models


class Tasks(models.Model):
    description = models.TextField(blank=True, null=True)
