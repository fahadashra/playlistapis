from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .playlistserializer import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
import json
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, logout

from rest_framework.decorators import api_view, permission_classes


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Add_Songs(request):
    if request.method == 'GET':
        book = Playlistsong.objects.all()
        serializer = AddsongSerializer(book, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddsongSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Add_Playlist(request):
    if request.method == 'GET':
        playlist = Playlist.objects.all()
        serializer = AddPlaylistSerializer(playlist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AddPlaylistSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def Delete_Song(request, pk):
    try:
        playlistsong = Playlistsong.objects.get(pk=pk)


    except Playlistsong.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddsongSerializer(playlistsong)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        playlistsong.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def Delete_Playlist(request, pk):
    try:
        playlist = Playlist.objects.get(pk=pk)

    except Playlistsong.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddPlaylistSerializer(playlist)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def GetAllSongsdetails(request):
    if request.method == 'GET':
        playlist = Playlistsong.objects.all()
        serializer = AddsongSerializer(playlist, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def GetAllPlaylistdetails(request):
    if request.method == 'GET':
        playlist = Playlist.objects.all()
        serializer = AddPlaylistSerializer(playlist, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def GetAllPlaylistbyid(request):
    if request.method == 'GET':
        user=request.user
        getuser = Playlist.objects.filter(user_id=user)
        serializer = AddPlaylistSerializer(getuser, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['GET', 'POST'])
def get_playlist_by_id(request, pk):
    try:
        playlist = Playlist.objects.get(pk=pk)
        print(playlist)

    except Playlist.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddPlaylistSerializer(playlist)
        return Response(serializer.data, status=200)


@api_view(['GET', 'POST'])
def Singlesong_detail(request, pk):
    try:
        playlistsong = Playlistsong.objects.get(pk=pk)

    except Playlistsong.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AddsongSerializer(playlistsong)
        return Response(serializer.data, status=200)


class RegisterPlaylistApi(APIView):
    serializer_class = RegisterSerialzierNew

    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        serializer = self.serializer_class(data=request.data)
        response = serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(email=(request.data.get('email').lower()),
                                        username=request.data.get('email'),
                                        first_name=first_name,
                                        last_name=last_name,
                                        )
        user.is_active = True
        user.set_password(request.data.get('password'))
        user.save()
        token = Token.objects.get_or_create(user=user)[0].key
        get_user = get_object_or_404(User, email=user.username)
        user_profile_serializer = RegisterSerialzierNew(get_user)
        user_profile_serializer = user_profile_serializer.data
        return Response(
            {"status_code": status.HTTP_200_OK, "success": True, "message": "user login success",
             "data": user_profile_serializer})


class PlaylistLoginApi(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        print("1")
        serializer = self.serializer_class(data=request.data)
        response = serializer.is_valid(raise_exception=True)
        print("2")
        return self.on_valid_request_data(serializer.validated_data, request)

    def on_valid_request_data(self, data, request):
        print("3")
        email = data.get('username')
        password = data.get('password')
        print("4")
        user_obj = User.objects.filter(username=email).last()
        if user_obj:
            try:
                user = authenticate(username=user_obj.username, password=password)
                if user is not None:
                    user_profile_serializer = UsereSerializer(user)
                    user_profile_serializer = user_profile_serializer.data
                    token, created = Token.objects.get_or_create(user=user)
                    response = {
                        'token': token.key,
                        'user_profile': user_profile_serializer
                    }
                    return Response(
                        {"status_code": status.HTTP_200_OK, "success": True, "message": "user login success",
                         "data": response})

                return Response(
                    {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "user login fail"})
            except Exception as e:
                return Response(
                    {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "user login fail"})

        else:
            return Response(
                {"status_code": status.HTTP_400_BAD_REQUEST, "success": False, "message": "user login fail"})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def User_logout(request):

    request.user.auth_token.delete()

    logout(request)

    return Response('User Logged out successfully')