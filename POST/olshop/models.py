from django.db import models

class Produk(models.Model):
    def __str__(self):
        return self.Nama
    Nama = models.CharField(max_length=200)
    harga = models.FloatField()
    diskon = models.FloatField()
    kategori = models.CharField(max_length=200)
    deskripsi = models.TextField()
    image = models.CharField(max_length=300)
    
class Order(models.Model):
    def __str__(self):
        return self.nama
    items = models.CharField(max_length=200)
    nama = models.CharField(max_length=200)
    email = models.CharField(max_length=300)
    alamat = models.CharField(max_length=300)
    provinsi = models.CharField(max_length=200)
    kota = models.CharField(max_length=300)
    kecamatan = models.CharField(max_length=300)
    kelurahan = models.CharField(max_length=300)
    kodepos = models.CharField(max_length=300)
    total = models.CharField(max_length=300)
