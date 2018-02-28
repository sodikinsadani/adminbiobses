from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from adminbiobses.models import Pengarang
from adminbiobses.forms import fPengarang
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class pengarang(View):
    form_class = (fPengarang)
    template_name = 'adminbiobses/pengarang.html'
    def get_pengarang(self):
        pengarang = Pengarang.objects.all()
        return pengarang

    def get(self, request):
        context = {
            'pengarang' : self.get_pengarang(),
            'form' : self.form_class,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            pengarang = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menambah {0} ke data pengarang
            '''.format(pengarang.nama_pengarang,))
            return HttpResponseRedirect(reverse('adminbiobses:pengarang'))
        else :
            messages.add_message(request, messages.warning, '''Gagal menambah data pengarang. Data tidak valid''')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class pengarangEdit(View):
    def get_pengarang(self, pk):
        pengarang = get_object_or_404(Pengarang, pk=pk)
        return pengarang

    def post(self, request, pk):
        pengarang = self.get_pengarang(pk)
        nama_pengarang = pengarang.nama_pengarang

        form = fPengarang(request.POST, instance=pengarang)
        if form.is_valid():
            pengarang = form.save()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil mengubah data {0} ke data pengarang
            '''.format(nama_pengarang,))
        else :
            messages.add_message(request, messages.SUCCESS, '''Gagal mengubah data pengarang ''')

        return redirect('adminbiobses:pengarang')

@method_decorator(login_required, name='dispatch')
class pengarangDelete(View):
    def get_pengarang(self, pk):
        pengarang = get_object_or_404(Pengarang, pk=pk)
        return pengarang

    def post(self, request, pk):
        pengarang = self.get_pengarang(pk)
        nama_pengarang = pengarang.nama_pengarang

        try :
            pengarang = pengarang.delete()
            messages.add_message(request, messages.SUCCESS, '''
            Berhasil menghapus {0} dari data pengarang
            '''.format(nama_pengarang,))
        except :
            messages.add_message(request, messages.SUCCESS, '''Gagal menghapus data pengarang ''')

        return redirect('adminbiobses:pengarang')
