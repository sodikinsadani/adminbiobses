from django.db import models
from .pengarang import Pengarang
from .penerbit import Penerbit
from .subkategori import SubKategori

class Buku(models.Model):
    nama_buku = models.CharField(max_length=100)
    pengarang = models.ForeignKey(Pengarang, on_delete=models.CASCADE,)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE,)
    subkategori = models.ForeignKey(SubKategori, on_delete=models.CASCADE,)
    harga = models.IntegerField()
    berat = models.FloatField(blank=True,null=True)
    diskon = models.FloatField(blank=True,null=True)
    image1 = models.FileField(upload_to='master buku/',blank=True,null=True)
    image2 = models.FileField(upload_to='master buku/',blank=True,null=True)
    image3 = models.FileField(upload_to='master buku/',blank=True,null=True)

    class Meta:
        ordering = ["subkategori","penerbit","pengarang","nama_buku"]

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.nama_buku)
