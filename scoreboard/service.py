def addOwners(data):
    for division in data['divisions']:
        for team in division['teams']:
            owners = team['owners']
            primary_owner_id = owners[0]
            if len(owners) > 1:
              for owner in owners:
                # more than more owner, find the non-todd owner
                if owner != '{D9A26600-179F-46F8-9101-DAE9AAC9A82A}':
                  primary_owner_id = owner
                  break
            primary_owner_name = ''
            for member in division['members']:
              if member['id'] == primary_owner_id:
                primary_owner_name = member['firstName'] + ' ' + member['lastName']
                break
            team['primaryOwner'] = primary_owner_name
    return data