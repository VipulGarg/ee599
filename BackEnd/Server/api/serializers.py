from rest_framework import serializers

from friends.models import FriendsConnectivity


class FriendsConnectivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendsConnectivity
        fields = ('name', 'idval', 'size', 'listf')

