from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
#create your vies here

def index(request):
    return render(request, 'irubot/index.html', {})

def room(request, room_name):
    return render(request, 'irubot/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
