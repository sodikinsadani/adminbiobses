from django.db import models

class SubKategori(models.Model):
    nama_sub_kategori = models.CharField(max_length=100)

    class Meta:
        ordering = ["nama_sub_kategori"]

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.nama_sub_kategori)
