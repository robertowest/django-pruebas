from django.contrib import admin

from apps.comunes.views import get_app_list
from .models import Localidad, Pais, Provincia

class ProvinciaInline(admin.TabularInline):
    model = Provincia
    fields = ['nombre', 'pais']
    list_display = ('nombre', 'pais')


class PaisAdmin(admin.ModelAdmin):
    fields = ['nombre']
    inlines = [ProvinciaInline]


class LocalidadInline(admin.TabularInline):
    model = Localidad
    fields = ['nombre', 'cpostal', 'provincia']
    list_display = ['nombre', 'cpostal', 'provincia']


class ProvinciaAdmin(admin.ModelAdmin):
    fields = ['nombre', 'pais']
    list_display = ['nombre', 'pais']
    list_filter = ['pais']
    inlines = [LocalidadInline]


class LocalidadAdmin(admin.ModelAdmin):
    fields = ['nombre', 'cpostal', 'provincia']
    search_fields = ['nombre']


admin.AdminSite.get_app_list = get_app_list

admin.site.register(Pais, PaisAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Localidad, LocalidadAdmin)


# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['sku', 'title', 'unit', 'unitCost', 'quantity']
#     list_filter = ('sku', 'unit')
#     #fields = [('family','location'),('sku','barcode'), ('title','description'),('unit', 'unitCost'), ('quantity','minQuantity')]
#     fieldsets = (
#         ('Section 1', {
#             'fields': ('family','location')
#         }),
#         ('Section 2', {
#             'fields': ('title','description')
#         }),
#         ('Section 3', {
#             'fields': ('sku','barcode','unit', 'unitCost','quantity','minQuantity')
#         }),
#     )