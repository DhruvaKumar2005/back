from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def index(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ItemForm()

    items = Item.objects.all()
    return render(request, 'index.html', {'form': form, 'items': items})

