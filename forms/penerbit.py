from django import forms
from adminbiobses.models import Penerbit

class fPenerbit(forms.ModelForm):
    class Meta:
        model = Penerbit
        fields = '__all__'