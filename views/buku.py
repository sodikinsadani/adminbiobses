from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from adminbiobses.models import Buku
from adminbiobses.forms import fBuku
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class buku(View):
    form_class = (fBuku)
    template_name = 'adminbiobses/buku.html'
    def get_buku(self):
        buku = Buku.objects.all()
        return buku

    def get(self, request):
        context = {
            'buku' : self.get_buku(),
            'form' : self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = fBuku(request.POST, request.FILES)
        
        if form.is_valid():
            buku = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menambah {0} ke data buku
            '''.format(buku.nama_buku,))
            return HttpResponseRedirect(reverse('adminbiobses:buku'))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal menambah data buku. Data tidak valid''')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class bukuEdit(View):
    def get_buku(self, pk):
        buku = get_object_or_404(Buku, pk=pk)
        return buku

    def post(self, request, pk):
        buku = self.get_buku(pk)
        nama_buku = buku.nama_buku

        form = fBuku(request.POST, instance=buku)
        if form.is_valid():
            buku = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} ke data buku
            '''.format(nama_buku,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data buku ''')

        return redirect('adminbiobses:buku')

@method_decorator(login_required, name='dispatch')
class bukuDelete(View):
    def get_buku(self, pk):
        buku = get_object_or_404(Buku, pk=pk)
        return buku

    def post(self, request, pk):
        buku = self.get_buku(pk)
        nama_buku = buku.nama_buku

        try :
            buku = buku.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data buku
            '''.format(nama_buku,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data buku ''')

        return redirect('adminbiobses:buku')
