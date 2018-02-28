from django import forms
from adminbiobses.models import SubKategori

class fSubKategori(forms.ModelForm):
    class Meta:
        model = SubKategori
        fields = '__all__'
        widgets = {}

    def __init__(self, *args, **kwargs):
        super(fSubKategori, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
