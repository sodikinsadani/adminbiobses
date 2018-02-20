from django.db import models

class Penerbit(models.Model):
    id_penerbit = models.AutoField(primary_key=True)
    nama_penerbit = models.CharField(max_length=100)