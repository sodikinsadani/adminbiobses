from django.urls import path
from . import views

app_name = 'adminbiobses'
urlpatterns = [
    path('login/', views.login_view.as_view(), name='login'),
    path('', views.index.as_view(), name='index'),
    path('logout/', views.logout_view.as_view(), name='logout'),
    path('buku/', views.buku.as_view(), name='buku'),
    path('buku/<int:pk>/edit/', views.bukuEdit.as_view(), name='bukuEdit'),
    path('buku/<int:pk>/delete/', views.bukuDelete.as_view(), name='bukuDelete'),
    path('penerbit/', views.penerbit.as_view(), name='penerbit'),
    path('penerbit/<int:pk>/edit/', views.penerbitEdit.as_view(), name='penerbitEdit'),
    path('penerbit/<int:pk>/delete/', views.penerbitDelete.as_view(), name='penerbitDelete'),
    path('kategori/', views.kategori.as_view(), name='kategori'),
    path('kategori/<int:pk>/edit/', views.kategoriEdit.as_view(), name='kategoriEdit'),
    path('kategori/<int:pk>/delete/', views.kategoriDelete.as_view(), name='kategoriDelete'),
    path('subkategori/', views.subKategori.as_view(), name='subkategori'),
    path('subkategori/<int:pk>/edit/', views.subKategoriEdit.as_view(), name='subkategoriEdit'),
    path('subkategori/<int:pk>/delete/', views.subKategoriDelete.as_view(), name='subkategoriDelete'),
    path('pengarang/', views.pengarang.as_view(), name='pengarang'),
    path('pengarang/<int:pk>/edit/', views.pengarangEdit.as_view(), name='pengarangEdit'),
    path('pengarang/<int:pk>/delete/', views.pengarangDelete.as_view(), name='pengarangDelete'),
]
