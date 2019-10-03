from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response

from espn import service
from season.models import Season
from standings.serializers import StandingSerializer
from standings.service import addOwners

import football_server.settings as settings

import pdb


def sortFunc(team):
    return team['playoffSeed']

# Create your views here.
@cache_page(60 * 5)
@api_view(['GET',])
def standings_view(request):

    season = Season.objects.get(year=settings.SEASON_ID)
    divisions = season.divisions.all()
    response = service.fetchStandings(divisions)
    addOwners(response['data'])

    for index, division in enumerate(response['data']['divisions']):
        val = division['teams']
        standings_serialized = StandingSerializer(val, many=True)
        response['data']['divisions'][index]['teams'] = sorted(standings_serialized.data, key=sortFunc)
        
        keys_to_keep = ['id', 'name', 'scoringPeriod', 'name', 'teams']
        subdict = {x: response['data']['divisions'][index][x] for x in keys_to_keep if x in response['data']['divisions'][index]}

        response['data']['divisions'][index] = subdict


    return Response(response['data'], response['status_code'])