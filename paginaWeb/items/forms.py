# items/forms.py
# items/forms.py
from django import forms
from productos.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'destacado', 'url']
