from rest_framework import serializers
from locations.models import LocationModel


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="locations:locationmodel-detail")
    class Meta:
        model = LocationModel
        # fields = ('url', 'id', 'taker', 'message') 
        fields = "__all__"


        