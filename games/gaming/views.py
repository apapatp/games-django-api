# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import Game
from .serializers import GameSerializer

class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)  # Render the dict to json.
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt  # Ensure the view sets a CSRF cookie. We will add security later.
def game_list(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_serializer = GameSerializer(games, many=True)  # The many arg is to signify to the serializer that multiple instances have to be serialized.
        return JSONResponse(game_serializer.data)

    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            # Save the Game to the table
            game_serializer.save()
            return JSONResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def game_detail(request, pk):
    '''

    :param request:
    :param pk:
    :return:
    '''

    # Try to get the contents and if not return an error
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return JSONResponse(game_serializer.data)

    if request.method == 'PUT':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(game, data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JSONResponse(game_serializer.data)
        return JSONResponse(game_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


    if request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

