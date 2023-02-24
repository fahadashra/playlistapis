from rest_framework import serializers
from .models import Playlistsong,Playlist
from django.contrib.auth.models import User


class AddsongSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = Playlistsong

        fields = '__all__'

class AddPlaylistSerializer(serializers.ModelSerializer):
    # id=serializers.IntegerField()
    class Meta:
        model = Playlist

        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50, required=True)
    password = serializers.CharField(max_length=50, required=True)

class RegisterSerialzierNew(serializers.Serializer):
    first_name=serializers.CharField(max_length=30,required=True)
    last_name=serializers.CharField(max_length=30,required=True)
    password=serializers.CharField(max_length=30,required=True)
    email=serializers.EmailField(required=True)

class UsereSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'