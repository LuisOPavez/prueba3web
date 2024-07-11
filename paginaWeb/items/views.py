# items/views.py
from django.shortcuts import render, get_object_or_404, redirect
from productos.models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()
    return render(request, 'items/item_list.html', {'items': items, 'user': request.user})


def item_detail(request, pk):
    item = get_object_or_404(Item, item=pk)  # Cambiamos a 'item' si es necesario
    return render(request, 'items/item_detail.html', {'item': item})

def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'items/item_form.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'items/item_edit.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('item_list')
    return render(request, 'items/item_confirm_delete.html', {'item': item})
