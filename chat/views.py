from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from chat.models import Room

# Create your views here.
def index(request):
    return HttpResponse("Hello, Jeremy")

def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'rooms/get.html', {'room': room})

def submit(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    try:
        text = request.POST['text']
    except KeyError:
        return render(request, 'rooms/get.html', {'room': room, 'error': 'No text submitted'})
    room.line_set.create(text=text)
    room.save()
    return HttpResponseRedirect(reverse('chat:room', args=(room.id,)))
