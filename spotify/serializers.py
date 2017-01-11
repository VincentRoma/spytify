from rest_framework import serializers
from .models import Spotify

class SpotifySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Spotify
        fields = ('url', 'username', 'email', 'is_staff')
