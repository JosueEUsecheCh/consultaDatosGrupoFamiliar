# principal/forms.py
from django import forms

class CedulaForm(forms.Form):
    ci_titular = forms.CharField(max_length=20, label='Cédula Titular')
