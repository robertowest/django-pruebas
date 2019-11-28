from datetime import datetime
from django.db import models

class AuditoriaModel(models.Model):
    class Meta:
        abstract = True

    def delete(self):
        self.active = False
        self.save()

    def hard_delete(self):
        super(AuditoriaModel, self).delete()

    def save(self, *args, **kwargs):
        self.modified = datetime.now()
        super(AuditoriaModel, self).save(*args, **kwargs)

    active = models.BooleanField('Activo', default=1)
    created = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True, blank=True)
    created_by = models.CharField('Creado por', max_length=15, editable=False, null=True, blank=True)
    updated = models.DateTimeField('Modificado', auto_now=True, editable=False, null=True, blank=True)
    updated_by = models.CharField('Modif. por', max_length=15, editable=False, null=True, blank=True)
