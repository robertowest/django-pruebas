from django.db import models


class StuffModel(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
