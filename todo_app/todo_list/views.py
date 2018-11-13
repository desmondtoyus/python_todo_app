from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item has been successfully added!'))
            return render(request, 'home.html', {'all_items':all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items':all_items})

def about(request):
    context = {'first_name': 'Desmond', 'last_name':'Ademiluyi', 'age':30}
    return render(request, 'about.html', context)

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('home')

def update(request, list_id):
    item = List.objects.get(pk=list_id)
    value = not item.completed
    item.completed = value
    item.save()
    messages.success(request, ('Item has been updated!'))
    return redirect('home')

def edit(request, list_id):
    if request.method =='POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance = item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been Edited!'))
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item':item})