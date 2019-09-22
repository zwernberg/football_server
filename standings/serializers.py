from rest_framework import serializers


class RecordSerializer(serializers.Serializer):
    wins = serializers.SerializerMethodField()
    losses = serializers.SerializerMethodField()
    ties = serializers.SerializerMethodField()
    pointsFor = serializers.SerializerMethodField()
    pointsAgainst = serializers.SerializerMethodField()

    def get_wins(self, obj):
      return (obj['overall']['wins'])
    def get_losses(self, obj):
      return (obj['overall']['losses'])
    def get_ties(self, obj):
      return (obj['overall']['ties'])
    def get_pointsFor(self, obj):
      return (int(obj['overall']['pointsFor']))
    def get_pointsAgainst(self, obj):
      return (int(obj['overall']['pointsAgainst']))

class StandingSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=200)
    id = serializers.IntegerField()
    nickname = serializers.CharField()
    abbrev = serializers.CharField()
    name = serializers.SerializerMethodField()
    playoffSeed = serializers.IntegerField()
    owners = serializers.CharField()
    points = serializers.IntegerField()
    record = RecordSerializer()


    def get_name(self, obj):
        return (obj['location'] + " " + obj['nickname'])

# gamesBack: 1
# losses: 1
# percentage: 0.5
# pointsAgainst: 190
# pointsFor: 201.78
# streakLength: 1
# streakType: "WIN"
# ties: 0
# wins: 1



# abbrev: "INTR"
# currentProjectedRank: 5
# divisionId: 0
# draftDayProjectedRank: 4
# id: 1
# isActive: false
# location: "The First"
# logo: "https://g.espncdn.com/lm-static/ffl/images/default_logos/6.svg"
# logoType: "VECTOR"
# nickname: "Intruder"
# owners: ["{D9A26600-179F-46F8-9101-DAE9AAC9A82A}", "{143097F5-5B51-49F4-B097-F55B51A9F40E}"]
# playoffSeed: 4
# points: 201.78
# pointsAdjusted: 0
# pointsDelta: 0
# primaryOwner: "{D9A26600-179F-46F8-9101-DAE9AAC9A82A}"
# rankCalculatedFinal: 0
# rankFinal: 0