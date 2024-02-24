from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import People
from .serializers import PeopleSerializer
from rest_framework.views import APIView

# Create your views here.
class PeopleAPIView(APIView):
    def get(self, request ):
        allPeople = People.objects.all()
        return Response({'peoples' : PeopleSerializer(allPeople , many=True).data})
    def post(self , request):
        serializer = PeopleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = People.objects.create(
            title = request.data['title'],
            content = request.data['content'],
            cat_id = request.data['cat_id']
        )
        return Response({'post':PeopleSerializer(post_new).data})

# class PeopleAPIView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer

