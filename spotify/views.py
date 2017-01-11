from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from .serializers import SpotifySerializer
from .models import Spotify
import requests
import spotipy


class SpotifyViewSet(viewsets.ModelViewSet):
    queryset = Spotify.objects.all()
    serializer_class = SpotifySerializer

    @list_route(methods=['get'])
    def history(self, request, pk=None):
        res = requests.get("http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=romavincent&api_key=7de59c64f2ea2d7b647c644da0dd795a&format=json")

        return Response(res.json(), 200)

    @list_route(methods=['get'])
    def playlists(self, request, pk=None):
        spotify = spotipy.Spotify(auth='97e5d655ede64c5fb6e314a9ca4efa0a')
        results = spotify.user_playlist('aixemple')
        import pdb; pdb.set_trace()
