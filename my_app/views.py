from django.shortcuts import render

def room_details(request): return render(request, 'index.html')
def rooms_list(request): return render(request, 'room_list.html')
