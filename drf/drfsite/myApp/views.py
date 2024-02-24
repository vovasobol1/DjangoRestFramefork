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
        serializer = PeopleSerializer(data=request.data) # входные данные были преобразованы в обьект сериализатор
        serializer.is_valid(raise_exception=True)

        serializer.save() #доабвлены в базу данных
        return Response({'post':serializer.data})

    def put(self , request , *args , **kwargs):
        pk = kwargs.get("pk", None )
        if not pk:
            return Response({'error' : 'method put not allowed'})

        try:
            instanse = People.objects.get(pk=pk)
        except:
            return Response({'error': 'обьект не найден'})

        serializer = PeopleSerializer(data=request.data , instance=instanse)# instanse это та запись которую нужно поменять
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, request , *args , **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': 'method put not allowed'})

        try:
            instanse = People.objects.get(pk=pk)
        except:
            return Response({'error': 'обьект не найден'})


        serializer = PeopleSerializer(data={'pk': pk})

        deleted = serializer.delete(instanse)
        if deleted:
            return Response({'success': 'Object deleted successfully'})
        else:
            return Response({'error': 'Failed to delete object'}, status=500)


# class PeopleAPIView(generics.ListAPIView):
#     queryset = People.objects.all()
#     serializer_class = PeopleSerializer

