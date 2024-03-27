from django.shortcuts import render
from .models import Reservation

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

def new(request):
    if request.method == 'POST':
        new_form = Reservation(request.POST)
        if new_form.is_valid():
            new_form.save()
            return redirect('reservations:create')
    else:
        new_form = Reservation()
    context = {
        'new_form': new_form
    }
    return render(request, 'reservations/new.html', context)

def create(request):
    if request.method == 'POST':
        create_form = Reservation(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('reservations:index')
    else:
        create_form = Reservation()
    context = {
        'create_form': create_form
    }
    return render(request, 'reservations/create.html', context)