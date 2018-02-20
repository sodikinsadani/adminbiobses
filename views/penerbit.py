from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(login_required, name='dispatch')
class penerbit(View):
    template_name = 'adminbiobses/penerbit.html'
    def get(self, request):
        return render(request, self.template_name)