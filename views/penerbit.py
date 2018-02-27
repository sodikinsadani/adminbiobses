from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from adminbiobses.models import Penerbit
from adminbiobses.forms import fPenerbit
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class penerbit(View):
    form_class = (fPenerbit)
    template_name = 'adminbiobses/penerbit.html'
    def get_penerbit(self):
        penerbit = Penerbit.objects.all()
        return penerbit

    def get(self, request):
        context = {
            'penerbit' : self.get_penerbit(),
            'form' : self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            penerbit = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menambah {0} ke data penerbit
            '''.format(penerbit.nama_penerbit,))
            return HttpResponseRedirect(reverse('adminbiobses:penerbit'))
        else :
            messages.add_message(request, messages.warning, '''Gagal menambah data penerbit. Data tidak valid''')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class penerbitEdit(View):
    def get_penerbit(self, pk):
        penerbit = get_object_or_404(Penerbit, pk=pk)
        return penerbit

    def post(self, request, pk):
        penerbit = self.get_penerbit(pk)
        nama_penerbit = penerbit.nama_penerbit

        form = fPenerbit(request.POST, instance=penerbit)
        if form.is_valid():
            penerbit = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} ke data penerbit
            '''.format(nama_penerbit,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data penerbit ''')

        return redirect('adminbiobses:penerbit')

@method_decorator(login_required, name='dispatch')
class penerbitDelete(View):
    def get_penerbit(self, pk):
        penerbit = get_object_or_404(Penerbit, pk=pk)
        return penerbit

    def post(self, request, pk):
        penerbit = self.get_penerbit(pk)
        nama_penerbit = penerbit.nama_penerbit

        try :
            penerbit = penerbit.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data penerbit
            '''.format(nama_penerbit,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data penerbit ''')

        return redirect('adminbiobses:penerbit')
