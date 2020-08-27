from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    birth_date = models.DateField()

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)
