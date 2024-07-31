from siakad.models import Mahasiswa
from django.contrib import admin

@admin.register(Mahasiswa)
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ('id_mahasiswa', 'nim', 'nama_mahasiswa', 'jenis_kelamin', 'program_studi')
    search_fields = ('nim', 'nama_mahasiswa')