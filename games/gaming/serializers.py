from rest_framework import serializers
from .models import Game

# class GameSerializer(serializers.Serializer):
#     '''
#     Declares the attributes that represent the fields that we want to be serialized
#     '''
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200)
#     release_date = serializers.DateTimeField()
#     game_category = serializers.CharField(max_length=200)
#     played = serializers.BooleanField(required=False)


# Going the Model Serializer route to remove duplicate code.
class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            'id',
            'name',
            'release_date',
            'game_category',
            'played'
        )
    def create(self, validated_data):
        '''
        Create a create method to create new Games
        :param validated_data: the data sent for us to serialize
        :return: a new game instance
        '''
        return Game.objects.create(**validated_data)


    def update(self, instance, validated_data):
        '''
        Method to
        :param instance:
        :param validated_data:
        :return: the instance to the call
        '''
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data('release_date', instance.release_date)
        instance.game_category = validated_data('game_category', instance.game_category)
        instance.played = validated_data('release_date', instance.played)
        instance.save() # save the update
        return instance