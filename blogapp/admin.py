from django.contrib import admin
from . import models
admin.site.site_header='Zaas Property'


# Register your models here.
class LogoModel(admin.ModelAdmin):
    list_display    = ["__str__","Title", "Status"]
    search_fields   = ['Title']
    list_per_page   = 20
    list_filter     = ["Title", "Status"]

admin.site.register(models.Logo, LogoModel)

