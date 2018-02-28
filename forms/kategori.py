from django import forms
from adminbiobses.models import Kategori

class fKategori(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = '__all__'
        widgets = {}

    def __init__(self, *args, **kwargs):
        super(fKategori, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
