def addOwners(data):
    for division in data['divisions']:
        for team in division['teams']:
            primary_owner_id = team['primaryOwner']
            primary_owner_name = ''

            for member in division['members']:
              if member['id'] == primary_owner_id:
                primary_owner_name = member['firstName'] + ' ' + member['lastName']
                break
            team['primaryOwner'] = primary_owner_name
    return data