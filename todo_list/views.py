from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, "Not Başarıyla Eklendi")
            return render(request, 'home.html', {'all_items' : all_items})
        else:
            messages.info(request, "Lütfen 1 ve 200 karakter arası bir not giriniz.")

    else:
        all_items = List.objects.all
        return render(request,"home.html", {'all_items': all_items})

    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})

def delete(request,list_id):
    item = List.objects.get(pk = list_id)
    item.delete()
    messages.warning(request, ("Not Başarıyla Silindi."))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk = list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk = list_id)

        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, "Not Başarıyla Güncellendi.")
            return redirect('home')
        else:
            messages.info(request, "Lütfen 1 ve 200 karakter arası bir not giriniz.")
        

    else:
        item = List.objects.get(pk = list_id)
        return render(request, 'edit.html', {'item': item})

    all_items = List.objects.all
    return render(request, 'home.html', {'all_items': all_items})