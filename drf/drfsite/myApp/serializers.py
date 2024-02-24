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

    def create(self, validated_data):
        return People.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title' ,instance.title )
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)

        instance.save()
        return instance

    def delete(self, instance=None):
        if instance:
            instance.delete()
            return True
        return False


# def encode():
#     model = PeopleModel('testPeople ', "testPeople_content")
#     modelSR = PeopleSerializer(model)
#     print(modelSR.data, type(modelSR.data), sep='\n')
#     json = JSONRenderer().render(modelSR.data)
#     print(json)

