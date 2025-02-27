# chat/views.py
from django.shortcuts import render


def index(request):
    return render(request, "df_chat/index.html")


def room(request, room_name):
    return render(request, "df_chat/room.html", {"room_name": room_name})
