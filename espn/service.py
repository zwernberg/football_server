import football_server.settings as settings
import requests

import pdb

def fetch(leagueId, seasonId = settings.SEASON_ID, params = {}, headers = {}):

    url = "https://fantasy.espn.com/apis/v3/games/FFL/seasons/" + str(seasonId) + '/segments/0/leagues/' + str(leagueId)
    print(url, params)
    return requests.get(url, params=params, headers=headers)

def fetchWeek(divisions):
  data = {
        'divisions': [],
    }
  status_code = ''

  params = {
    'view': [
      'mScoreboard',
      'mMatchupScore',
      'mTeam'
    ],
    'scoringPeriodId': 3
  }

  for division in divisions:
    headers = {'x-fantasy-filter': '{"schedule":{"filterCurrentMatchupPeriod":{"value":true}}}'}
    res = fetch(division.leagueId, params=params, headers=headers)

    val = res.json()

    val['name'] = division.name
    data['divisions'].append(val)
    status_code = res.status_code

  return {
    'data': data,
    'status_code': status_code
  }

def fetchStandings(divisions):
  data = {
        'divisions': [],
    }
  status_code = ''

  params = {
    'view': 'mTeam'
  }

  for division in divisions:

    res = fetch(division.leagueId, params=params)

    val = res.json()
    val['name'] = division.name
    data['divisions'].append(val)
    status_code = res.status_code

  return {
    'data': data,
    'status_code': status_code
  }
