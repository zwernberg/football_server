from django.shortcuts import render
from django.views.decorators.cache import cache_page

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from espn import service
from football_server import settings
from season.models import Season, Division

from scoreboard.service import addOwners, hydrateTeams

@cache_page(60)
@api_view(['GET',])
# Create your views here.
def scoreboard_view(request, seasonId=settings.SEASON_ID):
    season = Season.objects.get(year=seasonId)
    divisions = season.divisions.all()
    matchupPeriodId = request.GET.get('matchupPeriodId', '')
    response = service.fetchWeek(divisions)
    addOwners(response['data'])
    hydrateTeams(response['data'])

    for index, division in enumerate(response['data']['divisions']):
      keys_to_keep = ['id', 'name', 'schedule']
      subdict = {x: response['data']['divisions'][index][x] for x in keys_to_keep if x in response['data']['divisions'][index]}

      response['data']['divisions'][index] = subdict
    return Response(response['data'], response['status_code'])