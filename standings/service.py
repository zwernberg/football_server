def addOwners(data):
    for division in data['divisions']:
        for i in range(1, len(division['teams']) -1):
            team = division['teams'][i]
            teamIndex = team['id']
            owner = division['members'][teamIndex]['firstName'] + ' ' + division['members'][teamIndex]['lastName']
            team['owners'] = owner
    return data