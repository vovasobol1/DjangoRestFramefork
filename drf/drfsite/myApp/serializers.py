from rest_framework import serializers


from rest_framework.renderers import JSONRenderer

from .models import People

# class PeopleModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class PeopleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# def encode():
#     model = PeopleModel('testPeople ', "testPeople_content")
#     modelSR = PeopleSerializer(model)
#     print(modelSR.data, type(modelSR.data), sep='\n')
#     json = JSONRenderer().render(modelSR.data)
#     print(json)

