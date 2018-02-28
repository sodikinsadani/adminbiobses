from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from adminbiobses.models import SubKategori
from adminbiobses.forms import fSubKategori
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class subKategori(View):
    form_class = (fSubKategori)
    template_name = 'adminbiobses/sub_kategori.html'
    def get_sub_kategori(self):
        subkategori = SubKategori.objects.all()
        return subkategori

    def get(self, request):
        context = {
            'subkategori' : self.get_sub_kategori(),
            'form' : self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            subkategori = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menambah {0} ke data sub kategori
            '''.format(subkategori.nama_sub_kategori,))
            return HttpResponseRedirect(reverse('adminbiobses:subkategori'))
        else :
            messages.add_message(request, messages.warning, '''Gagal menambah data kategori. Data tidak valid''')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class subKategoriEdit(View):
    def get_sub_kategori(self, pk):
        subkategori = get_object_or_404(SubKategori, pk=pk)
        return subkategori

    def post(self, request, pk):
        subkategori = self.get_sub_kategori(pk)
        nama_sub_kategori = subkategori.nama_sub_kategori

        form = fSubKategori(request.POST, instance=subkategori)
        if form.is_valid():
            subkategori = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} ke data sub kategori
            '''.format(nama_sub_kategori,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data kategori ''')

        return redirect('adminbiobses:subkategori')

@method_decorator(login_required, name='dispatch')
class subKategoriDelete(View):
    def get_sub_kategori(self, pk):
        subkategori = get_object_or_404(SubKategori, pk=pk)
        return subkategori

    def post(self, request, pk):
        subkategori = self.get_sub_kategori(pk)
        nama_sub_kategori = subkategori.nama_sub_kategori

        try :
            subkategori = subkategori.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data sub kategori
            '''.format(nama_sub_kategori,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data kategori ''')

        return redirect('adminbiobses:subkategori')
