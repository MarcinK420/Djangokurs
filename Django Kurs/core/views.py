from django.shortcuts import render, redirect
from .forms import ServiceForm
from .models import Service
from datetime import datetime

def home(request):
    uslugi = Service.objects.all()  # pobierz wszystkie usługi z bazy
    context = {
        'imie': 'Kamil',
        'aktualny_czas': datetime.now(),
        'uslugi': uslugi,
        'now': datetime.now()
    }
    return render(request, 'core/home.html', context)

def about(request):
    context = {
        'now': datetime.now()
    }
    return render(request, 'core/about.html', context)

def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # przekieruj na stronę główną po dodaniu
    else:
        form = ServiceForm()
    return render(request, 'core/add_service.html', {'form': form})