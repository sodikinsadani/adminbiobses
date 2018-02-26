from django.contrib import admin
from adminbiobses.models import Penerbit

class PenerbitAdmin(admin.ModelAdmin):
    list_display = ('nama_penerbit','alamat','profile')

admin.site.register(Penerbit,PenerbitAdmin)
