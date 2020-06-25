# Django
from django import forms

#Models
from .models import Artist


class ArtistForm(forms.ModelForm):
    """."""
    class Meta:
        model = Artist
        fields = ("name", "image")
    
    def clean(self):
        try:
            sc=Artist.objects.get(name=self.cleaned_data['name'])
            if not self.instance.pk:
                raise forms.ValidationError("Registro ya existe")
            elif self.instance.pk != sc.pk:
                raise forms.ValidationError("Cambio no permitido")
        except Artist.DoesNotExist:
            pass
        return self.cleaned_data
           
           
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        self.fields['image'].required = False 
