from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from espn import service
from football_server import settings
from season.models import Season, Division

from scoreboard.service import addOwners

@api_view(['GET',])
# Create your views here.
def scoreboard_view(request, seasonId=settings.SEASON_ID):
    season = Season.objects.get(year=seasonId)
    divisions = season.divisions.all()
    matchupPeriodId = request.GET.get('matchupPeriodId', '')
    response = service.fetchWeek(divisions)
    # result = addOwners(response)
    return Response(response['data'], response['status_code'])