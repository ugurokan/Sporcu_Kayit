from django.db import models


class Brans(models.Model):
    Brans_Adı = models.CharField(max_length=30, blank=False, null=False)
    Ekleme_Tarihi = models.DateField()

    def __str__(self):
        return self.Brans_Adı
    class Meta:
        verbose_name = "Branş"
        verbose_name_plural  = "Branşlar"

class Antrenor(models.Model):
    Kimlik_Numarası = models.CharField(max_length=30, blank=False, null=False)
    Ad = models.CharField(max_length=30, blank=False, null=False)
    Soyad = models.CharField(max_length=30, blank=False, null=False)
    Telefon = models.CharField(max_length=30, blank=False, null=False)
    Branslar = models.ManyToManyField(Brans, blank=False)

    def __str__(self):
        return self.Ad
    class Meta:
        verbose_name = "Antrenor"
        verbose_name_plural  = "Antrenorler"


class Sporcu(models.Model):
    Kimlik_Numarası = models.CharField(max_length=30, blank=False, null=False)
    Ad = models.CharField(max_length=30, blank=False, null=False)
    Soyad = models.CharField(max_length=30, blank=False, null=False)
    Dogum = models.DateField(null=False)
    Okulu = models.CharField(max_length=30, blank=False, null=False)
    VeliAdSoyad = models.CharField(max_length=30, blank=False, null=False)
    Telefon = models.CharField(max_length=30, blank=False, null=False)
    Adres = models.CharField(max_length=120, blank=False, null=False)
    Email = models.CharField(max_length=30, blank=False, null=False)
    Branslar = models.ManyToManyField(Brans, blank=False)
    Antrenorler = models.ManyToManyField(Antrenor, blank=False)

    def __str__(self):
        return self.Ad
    class Meta:
        verbose_name = "Sporcu"
        verbose_name_plural  = "Sporcular"

