from django.db import models

class Mahasiswa(models.Model):
    # Define the fields
    id_mahasiswa = models.AutoField(primary_key=True)  # Auto-increment primary key
    nim = models.CharField(max_length=7)  # NIM with a max length of 7 characters
    nama_mahasiswa = models.CharField(max_length=50)  # Student name with a max length of 50 characters
    jenis_kelamin = models.CharField(max_length=12)  # Gender with a max length of 12 characters
    program_studi = models.CharField(max_length=25)  # Study program with a max length of 25 characters

    def __str__(self):
        return self.nama_mahasiswa