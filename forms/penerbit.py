from django import forms
from adminbiobses.models import Penerbit

class fPenerbit(forms.ModelForm):
    class Meta:
        model = Penerbit
        fields = '__all__'
        widgets = {
            'alamat':forms.Textarea(attrs={'rows':3,}),
            'profile':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fPenerbit, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
