from django.contrib.auth.models import User, Group
from rest_framework import serializers
from deck_app import models

from deck_app.models import Deck, DeckCard, UserDeck




class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username','email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class DeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'


class DeckCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeckCard
        fields = '__all__'

class UserDeckSerializer(serializers.HyperlinkedModelSerializer):
    sideDeck = DeckSerializer()
    mainDeck = DeckSerializer()
    extraDeck = DeckSerializer()
    class Meta:
        model = UserDeck
        fields = '__all__'

class UserDeckDeepSerializer(serializers.HyperlinkedModelSerializer):
    sideDeck = DeckSerializer()
    mainDeck = DeckSerializer()
    extraDeck = DeckSerializer()
    class Meta:
        model = UserDeck
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        #print(validated_data.pop("sideDeck"))
        sideDeck = models.Deck.objects.create(**validated_data.pop("sideDeck"))
        extraDeck = models.Deck.objects.create(**validated_data.pop("extraDeck"))
        mainDeck = models.Deck.objects.create(**validated_data.pop("mainDeck"))
        userDeck = models.UserDeck.objects.create(sideDeck=sideDeck,
                                                  extraDeck=extraDeck,
                                                  mainDeck=mainDeck,
                                                  id_owner = validated_data.pop("id_owner"),
                                                  stats_id = validated_data.pop("stats_id"),
                                                  name = validated_data.pop("name"))
        return userDeck

