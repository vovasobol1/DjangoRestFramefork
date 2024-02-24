from rest_framework import serializers

from myApp.models import People


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('title','cat_id')