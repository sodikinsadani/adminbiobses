from django import forms
from adminbiobses.models import Pengarang

class fPengarang(forms.ModelForm):
    class Meta:
        model = Pengarang
        fields = '__all__'
        widgets = {
            'profile':forms.Textarea(attrs={'rows':3,}),
        }

    def __init__(self, *args, **kwargs):
        super(fPengarang, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
