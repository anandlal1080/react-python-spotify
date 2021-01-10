from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerialzer
from .models import Room

# Create your views here.


class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerialzer
