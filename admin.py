from django.contrib import admin
from adminbiobses.models import Penerbit

class PenerbitAdmin(admin.ModelAdmin):
    list_display = ('id_penerbit','nama_penerbit')

admin.site.register(Penerbit,PenerbitAdmin)