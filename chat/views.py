from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from chat.models import Room

import pusher
p = pusher.Pusher(
  app_id='65252',
  key='0e0c5944e77aaa1238f8',
  secret='6fbab91e75fd738c2386'
)

# Create your views here.
def index(request):
    return HttpResponse("Hello, Jeremy")

def room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    return render(request, 'rooms/get.html', {'room': room, 'lines': room.line_set.order_by('timestamp')})

def submit(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    try:
        text = request.POST['text']
    except KeyError:
        return render(request, 'rooms/get.html', {'room': room, 'error': 'No text submitted'})
    room.line_set.create(text=text)
    room.save()
    p['room' + room_id].trigger('new_message', {'message': text})
    return HttpResponseRedirect(reverse('chat:room', args=(room_id,)))
