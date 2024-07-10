from django.db import models
from django.urls import reverse

class Item(models.Model):
    item = models.CharField(primary_key=True, max_length=8, editable=False)
    nombre = models.CharField(max_length=20)
    tipo_articulo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, help_text="Descuento en porcentaje")
    precio_desc = models.DecimalField(max_digits=20, decimal_places=2, editable=False)
    smart = models.BooleanField(default=False)
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='imagenes/')
    descripcion = models.CharField(max_length=500, default='Descripción no disponible')
    destacado = models.BooleanField(default=False)
    url = models.CharField(max_length=100, default='default-url')

    def save(self, *args, **kwargs):
        if not self.item:
            last_item = Item.objects.all().order_by('item').last()
            if not last_item:
                self.item = '00000001'
            else:
                item_int = int(last_item.item)
                new_item_int = item_int + 1
                self.item = f'{new_item_int:08d}'

        self.precio_desc = self.precio - (self.precio * (self.descuento / 100))
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre

    @property
    def absolute_url(self):
        return reverse(self.url)

    def formatted_precio(self):
        return "${:,.0f}".format(self.precio).replace(',', '.')
    
    def formatted_precio_desc(self):
        return "${:,.0f}".format(self.precio_desc).replace(',', '.')





