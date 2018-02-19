from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

class login_view(View):
    template_name = 'adminbiobses/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user =authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None :
            if user.is_active :
                try :
                    login(request, user)
                    request.session['user_id'] = user.id
                    request.session['username'] = user.username
                    request.session['name'] = user.first_name+' '+user.last_name or ''
                except :
                    messages.add_message(request, messages.INFO, 'Anda belum terdaftar, silahkan hubungi administrator')
                return redirect('adminbiobses:index')
            else :
                messages.add_message(request, messages.INFO, 'user belum terverifikasi')
        else :
            messages.add_message(request, messages.INFO, 'user atau password anda salah')
        
        return render(request, self.template_name)

class logout_view(View):
    def get(self, request):
        logout(request)
        return redirect('adminbiobses:login')

@method_decorator(login_required, name='dispatch')
class index(View):
    template_name = 'adminbiobses/index.html'
    def get(self, request):
        return render(request, self.template_name)
    