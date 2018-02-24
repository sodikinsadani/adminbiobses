from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from adminbiobses.models import Penerbit
from adminbiobses.forms import fPenerbit

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