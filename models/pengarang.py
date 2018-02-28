from django.db import models

class Pengarang(models.Model):
    nama_pengarang = models.CharField(max_length=100)
    profile = models.TextField(max_length=200,blank=True,null=True)

    class Meta:
        ordering = ["nama_pengarang"]


    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.nama_pengarang)
