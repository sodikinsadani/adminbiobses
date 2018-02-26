from django.shortcuts import render, redirect
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
