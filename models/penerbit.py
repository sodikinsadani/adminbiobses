from django.db import models

class Penerbit(models.Model):
    nama_penerbit = models.CharField(max_length=100)
    alamat = models.TextField(max_length=200,blank=True,null=True)
    profile = models.TextField(max_length=200,blank=True,null=True)

    class Meta:
        ordering = ["nama_penerbit"]

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.nama_penerbit)
