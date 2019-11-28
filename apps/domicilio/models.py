from django.db import models

from apps.comunes import models as Comunes

class Pais(Comunes.AuditoriaModel):
    class Meta:
        verbose_name = 'Pais'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=40, blank=True, null=True)


class Provincia(Comunes.AuditoriaModel):
    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=40, blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)


class Localidad(Comunes.AuditoriaModel):
    class Meta:
        verbose_name = 'Domicilio'
        verbose_name_plural = 'Domicilios'

    def __str__(self):
        return self.nombre

    nombre = models.CharField(max_length=40)
    cpostal = models.CharField(max_length=12, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)


class PaisesView(models.Model):
    pais_id = models.IntegerField(blank=True, null=True)
    pais = models.CharField(max_length=40, blank=True, null=True)
    prov_id = models.IntegerField(blank=True, null=True)
    provincia = models.CharField(max_length=40, blank=True, null=True)
    loc_id = models.IntegerField(blank=True, null=True)
    localidad = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'paises_view'


