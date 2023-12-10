from django.db import models
from django.urls import reverse

class daftarPeserta(models.Model):
    nama        = models.CharField(("Nama Mahasiswa"), max_length=50)
    sekolah     = models.CharField(("Asal Sekolah"), max_length=50)
    jurusan     = models.CharField(("Jurusan"), max_length=50)
    hp          = models.CharField(("No HP"), max_length=15)
    alamat      = models.CharField(("Alamat"), max_length=100)
    
    
    def __str__(self):
        return "{} jurusan {}".format(self.nama, self.jurusan)
    
    
    def get_absolute_url(self):
        return reverse("home")
    