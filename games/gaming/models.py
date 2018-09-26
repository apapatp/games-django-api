# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models

class Game(models.Model):
    '''
    Setting up the game model for the api
    '''
    class Meta:
        ordering = ('name', )

    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, blank=True, default='')
    played = models.BooleanField(default=False)
    release_date = models.DateTimeField()
    game_category = models.CharField(max_length=200, blank=True, default='')