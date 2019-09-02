from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from deck_app.serializers import UserSerializer, GroupSerializer, DeckSerializer, DeckCardSerializer, UserDeckSerializer, UserDeckDeepSerializer
from deck_app.models import Deck, DeckCard, UserDeck

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewd or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DeckViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows decks to be created, viewed or edited
    GET: /decks/ : all decks
    GET /decks/{idDeck} : get info for a deck, with Id
    POST /decks/ : create a new deck
    PUT /decks/{idDeck} : edit a specified Deck
    """
    queryset = Deck.objects.all().order_by('-date')
    serializer_class = DeckSerializer

class DeckCardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows decks to be created, viewed or edited
    GET: /decks/ : all decks
    GET /decks/{idDeck} : get info for a deck, with Id
    POST /decks/ : create a new deck
    PUT /decks/{idDeck} : edit a specified Deck
    """
    queryset = DeckCard.objects.all().order_by('-date')
    serializer_class = DeckCardSerializer

class UserDeckViewSet(viewsets.ModelViewSet):
    serializer_class = UserDeckSerializer
    queryset = UserDeck.objects.all().order_by('-date')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserDeckDeepSerializer
        else:
            return UserDeckSerializer