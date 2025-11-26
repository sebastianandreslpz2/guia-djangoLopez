from django import forms


class CrearNotebook(forms.Form):
    modelo = forms.CharField(max_length=50)
    procesador = forms.CharField(max_length=50)
    imagen = forms.ImageField(required=False)
    ram = forms.CharField(max_length=50)
    


class BuscarNotebook(forms.Form):
    modelo = forms.CharField(max_length=50, required=False)
    
    