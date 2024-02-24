from django.shortcuts import render
from rest_framework import generics
from .models import People
from .serializers import PeopleSerializer


# Create your views here.
class PeopleAPIView():



# class PeopleAPIView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer

