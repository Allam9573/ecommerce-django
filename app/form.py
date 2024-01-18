from django import forms


class FormularioArticulo(forms.Form):
    nombre = forms.CharField(
        label='Nombre'
    )
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    fabricante = forms.CharField(max_length=50)
