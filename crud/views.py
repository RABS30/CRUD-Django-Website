from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, View


from . import models
from . import forms

# ========== Class base View ==========
# read
class home(View):
    template_name = "crud/home.html"
    data_peserta = models.daftarPeserta.objects.all()
    context ={
        "object_list"   : data_peserta,
        "title"         : "Daftar Peserta"
    }
    
    def get(self, request):
        return render(request, self.template_name, self.context)
   
    
# create  
class dataPesertaBaru(CreateView):
    model           = models.daftarPeserta
    form_class      = forms.formDaftarPeserta


# update  
class updateDataPeserta(UpdateView):
    model           = models.daftarPeserta
    form_class      = forms.formDaftarPeserta
    
     
# hapus  
class deleteDataPeserta(DeleteView):
    model           = models.daftarPeserta
    
    success_url     = reverse_lazy("home")
    
    
    # Halaman utama (function base view)



# ========== Function base view ==========

# read
def home(request):
    data_peserta    = models.daftarPeserta.objects.all()
    
    context         = {
        "object_list"   : data_peserta,
        "title"         : "Daftar Peserta"
    }
    return render(request, "crud/home.html", context)

# create
def dataPesertaBaru(request):
    forms_peserta   = forms.formDaftarPeserta 
    if request.method == "POST" :
        form = forms.formDaftarPeserta(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("home"))
        return redirect(reverse_lazy("daftar"))
    context         = {
        "form": forms.formDaftarPeserta
    }
    return render(request,"crud/daftarpeserta_form.html", context)
    
# update
def updateDataPeserta(request,id):
    object      = models.daftarPeserta.objects.get(pk=id)
    
    data    = {
        "nama"      : object.nama,
        "sekolah"   : object.sekolah,
        "jurusan"   : object.jurusan,
        "hp"        : object.hp,
        "alamat"    : object.alamat
    }
    
    form_akun = forms.formDaftarPeserta(request.POST or None, initial=data, instance=object)
    
    if request.method == "POST":
        if form_akun.is_valid():
            form_akun.save()
        return redirect("home")

    context = {
        "title"     : "edit data",
        "object"    : object,
        "form"      : form_akun 
    }
    return render(request, "crud/daftarpeserta_form.html",context)

#  delete
def deleteDataPeserta(request, pk):
    models.daftarPeserta.objects.get(id=pk).delete()
    return redirect(reverse_lazy("home"))




 






























