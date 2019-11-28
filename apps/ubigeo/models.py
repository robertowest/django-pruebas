from django.db import models


class Region(models.Model):
    """Regiones"""
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nombre


class Provincia(models.Model):
    """Provincias"""
    region = models.ForeignKey(Region, models.DO_NOTHING)
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nombre


class Distrito(models.Model):
    """Distritos"""
    provincia = models.ForeignKey(Provincia, models.DO_NOTHING)
    codigo = models.PositiveSmallIntegerField()
    nombre = models.CharField(max_length=40)

    def __unicode__(self):
        return self.nombre
