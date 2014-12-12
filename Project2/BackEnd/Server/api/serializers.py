from rest_framework import serializers

from friends.models import FriendsConnectivity
from friends.models import TimeData
from friends.models import ModelData
from friends.models import VennIntersectionData


class FriendsConnectivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsConnectivity
        fields = ('name', 'idval', 'size', 'listf')
			
class TimeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeData
        fields = ('time', 'count')
		
class ModelDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelData
        fields = ('changeingrowthrate', 'count')
		
class VennIntersectionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VennIntersectionData
        fields = ('facebook', 'twitter', 'intersection')

