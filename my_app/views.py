from django.shortcuts import get_object_or_404, render
from .models import Rooms

def rooms_list(request):
    rooms = Rooms.objects.all()
    context = {'rooms': rooms}
    return render(request, 'rooms_list.html', context)

def room_details(request, pk):
    room = get_object_or_404(Rooms, pk=pk)
    context = {'room' : room}
    return render(request, 'room_details.html', context)
