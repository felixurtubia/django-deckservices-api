from django.test import TestCase
from deck_app.models import DeckCard, Deck, UserDeck


# Create your tests here.
class DeckTestCase(TestCase):
    def setUp(self) -> None:
        userDeck = UserDeck.objects.create()
        userDeck.id_owner = 1
        userDeck.stats_id = 1
        userDeck.mainDeck = Deck.objects.create(name="Mazo de prueba, main deck 1")
        userDeck.sideDeck = Deck.objects.create(name="Mazo de prueba, side deck 1")
        userDeck.extraDeck = Deck.objects.create(name="Mazo de prueba, extra deck 1")

    def test_deck_can_be_created_and_retrieved(self):
        deck_1 = UserDeck.objects.filter(id_owner=1)[0]
        self.assertEqual(deck_1.mainDeck, "Mazo de prueba, main deck 1")
        self.assertEqual(deck_1.mainDeck(), "Mazo de prueba, side deck 1")