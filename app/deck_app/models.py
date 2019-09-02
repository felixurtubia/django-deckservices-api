from django.db import models
from django.contrib.auth.models import User


class Deck(models.Model):
    cardsMin= models.IntegerField(default=-1)
    cardsMax = models.IntegerField(default=-1)
    cardsCount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def my_cards(self):
        return self.deckCard.all()

    def __str__(self):
        return "This deck has {} cards".format(self.cardsCount)

class DeckCard(models.Model):
    cardId = models.IntegerField()
    cardURI = models.URLField()
    date = models.DateTimeField(auto_now_add=True)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name='deckCard')

class UserDeck(models.Model):
    id_owner = models.IntegerField(default=-1)
    name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    stats_id = models.IntegerField(default=-1)
    sideDeck = models.OneToOneField(Deck,
                                    on_delete=models.CASCADE,
                                    primary_key=False, related_name="sideDeck")
    mainDeck = models.OneToOneField(Deck,
                                    on_delete=models.CASCADE,
                                    primary_key=False, related_name="mainDeck")
    extraDeck = models.OneToOneField(Deck,
                                    on_delete=models.CASCADE,
                                    primary_key=False, related_name="extraDeck")