from django import forms
from adminbiobses.models import Buku

class fBuku(forms.ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'
        widgets = {
            'isi_berita':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fBuku, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
