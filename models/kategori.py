from django.db import models

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100)

    class Meta:
        ordering = ["nama_kategori"]

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.nama_kategori)
