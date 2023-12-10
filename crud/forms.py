from django import forms

from . import models

class formDaftarPeserta(forms.ModelForm):
    class Meta:
        model   = models.daftarPeserta
        fields  = "__all__"
        
        widgets = {
            "nama"      : forms.TextInput(attrs={"class":"form-control"}),
            "sekolah"   : forms.TextInput(attrs={"class":"form-control"}),
            "jurusan"   : forms.TextInput(attrs={"class":"form-control"}),
            "hp"        : forms.NumberInput(attrs={"class":"form-control"}),
            "alamat"    : forms.TextInput(attrs={"class":"form-control"}),
        }