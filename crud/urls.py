from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", views.home.as_view(), name="home"),
    # path("daftar_peserta_baru/", views.dataPesertaBaru.as_view(), name="daftar"),
    # path("edit/<pk>", views.updateDataPeserta.as_view(), name="update"),
    # path("hapus/<pk>", views.deleteDataPeserta.as_view(), name="delete"),
    
    path("", views.home, name="home"),
    path("daftar_peserta_baru/", views.dataPesertaBaru, name="daftar"),
    path("edit/<str:id>", views.updateDataPeserta, name="update"),
    path("hapus/<pk>", views.deleteDataPeserta, name="delete"),
    
    
]
