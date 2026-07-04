from django.shortcuts import get_object_or_404, redirect, render
from .models import Rooms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, login

def rooms_list(request):
    rooms = Rooms.objects.all()
    context = {'rooms': rooms}
    return render(request, 'rooms_list.html', context)

def room_details(request, pk):
    room = get_object_or_404(Rooms, pk=pk)
    context = {'room' : room}
    return render(request, 'room_details.html', context)

def login_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.get_user()
            login(request, user)
            return redirect('rooms_list')
    else: form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
