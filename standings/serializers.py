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
    primaryOwner = serializers.CharField()
    points = serializers.IntegerField()
    record = RecordSerializer()


    def get_name(self, obj):
        return (obj['location'] + " " + obj['nickname'])
