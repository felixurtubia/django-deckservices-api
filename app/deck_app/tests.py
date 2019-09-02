from django.test import TestCase
from deck_app.models import DeckCard, Deck, UserDeck


# Create your tests here.
class DeckTestCase(TestCase):
    def setUp(self) -> None:
        userDeck = UserDeck.objects.create()
        userDeck.id_owner = 1
        userDeck.stats_id = 1
        userDeck.mainDeck = Deck.objects.create(cardsMin=0, cardsMax=15, cardsCount=0)
        userDeck.sideDeck = Deck.objects.create(cardsMin=0, cardsMax=15, cardsCount=0)
        userDeck.extraDeck = Deck.objects.create(cardsMin=0, cardsMax=15, cardsCount=0)

    def test_deck_can_be_created_and_retrieved(self):
        deck_1 = UserDeck.objects.filter(id_owner=1)[0]
        self.assertEqual(deck_1.mainDeck, "This deck has 0 cards")
        self.assertEqual(deck_1.mainDeck(), "This deck has 0 cards")