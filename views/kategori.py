from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from adminbiobses.models import Kategori
from adminbiobses.forms import fKategori
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class kategori(View):
    form_class = (fKategori)
    template_name = 'adminbiobses/kategori.html'
    def get_kategori(self):
        kategori = Kategori.objects.all()
        return kategori

    def get(self, request):
        context = {
            'kategori' : self.get_kategori(),
            'form' : self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            kategori = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menambah {0} ke data kategori
            '''.format(kategori.nama_kategori,))
            return HttpResponseRedirect(reverse('adminbiobses:kategori'))
        else :
            messages.add_message(request, messages.warning, '''Gagal menambah data kategori. Data tidak valid''')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class kategoriEdit(View):
    def get_kategori(self, pk):
        kategori = get_object_or_404(Kategori, pk=pk)
        return kategori

    def post(self, request, pk):
        kategori = self.get_kategori(pk)
        nama_kategori = kategori.nama_kategori

        form = fKategori(request.POST, instance=kategori)
        if form.is_valid():
            kategori = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} ke data kategori
            '''.format(nama_kategori,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data kategori ''')

        return redirect('adminbiobses:kategori')

@method_decorator(login_required, name='dispatch')
class kategoriDelete(View):
    def get_kategori(self, pk):
        kategori = get_object_or_404(Kategori, pk=pk)
        return kategori

    def post(self, request, pk):
        kategori = self.get_kategori(pk)
        nama_kategori = kategori.nama_kategori

        try :
            kategori = kategori.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data kategori
            '''.format(nama_kategori,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data kategori ''')

        return redirect('adminbiobses:kategori')
