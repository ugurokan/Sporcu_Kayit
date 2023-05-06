from django.contrib import admin
from .models import Antrenor, Sporcu, Brans


class AntrenorAdmin(admin.ModelAdmin):
    list_display = ['Kimlik_Numarası', 'Ad', 'Soyad', 'Telefon']
    search_fields = ['Kimlik_Numarası']
    list_filter = ['Branslar']


class SporcuAdmin(admin.ModelAdmin):
    list_display = ['Kimlik_Numarası', 'Ad', 'Soyad', 'Telefon', 'Dogum']
    search_fields = ['Kimlik_Numarası']
    list_filter = ['Branslar']


admin.site.register(Antrenor, AntrenorAdmin)
admin.site.register(Sporcu, SporcuAdmin)
admin.site.register(Brans)
admin.site.site_header = 'Spor Kayıt Sistemi'