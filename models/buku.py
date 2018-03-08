from django.db import models
from .pengarang import Pengarang
from .penerbit import Penerbit
from .kategori import Kategori
from .subkategori import SubKategori
from django.utils import timezone

class Buku(models.Model):
    nama_buku = models.CharField(max_length=100)
    pengarang = models.ForeignKey(Pengarang, on_delete=models.SET_NULL, null=True)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.SET_NULL, null=True)
    subkategori = models.ForeignKey(SubKategori, on_delete=models.SET_NULL, null=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    harga = models.IntegerField()
    harga_diskon = models.IntegerField()
    tahun_terbit = models.IntegerField()
    tebal_buku = models.FloatField(blank=True,null=True)
    berat = models.FloatField(blank=True,null=True)
    stok = models.IntegerField()
    diskon = models.FloatField(blank=True,null=True)
    isi_berita = models.TextField(max_length=200,blank=True,null=True)
    image1 = models.FileField(upload_to='master buku/',blank=True,null=True)
    image2 = models.FileField(upload_to='master buku/',blank=True,null=True)
    image3 = models.FileField(upload_to='master buku/',blank=True,null=True)

    class Meta:
        ordering = ["subkategori","penerbit","pengarang","nama_buku"]

    def __str__(self): # __unicode__ on Python 2
        return '{}'.format(self.nama_buku)
