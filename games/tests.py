from django.test import TestCase
from django.urls import reverse

from .models import Game


class GameTests(TestCase):
    """A class for testing the games app."""

    @classmethod
    def setUpTestData(cls):
        """A function for setting test data"""
        cls.game = Game.objects.create(
            title="Ajax-Real M",
            description="Лига Чемпионов 2018-2019 1 8 финала Первый матч.",
            video="https://www.youtube.com/watch?v=kCgrQBtsRG4",
            image="i.jpeg",
        )

    def test_game_listing(self):
        """Checks that both its string
        representation and content are correct."""
        self.assertEqual(f"{self.game.title}", "Ajax-Real M")
        self.assertEqual(
            f"{self.game.description}",
            "Лига Чемпионов 2018-2019 1 8 финала Первый матч.",
        )

    def test_game_list_view(self):
        """
        Confirms that our main page returns the
        HTTP 200 status code, contains our text,
        and uses the correct one. games/game_list.html
        the template.
        """
        response = self.client.get(reverse("game_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ajax-Real M")
        self.assertTemplateUsed(response, "games/game_list.html")

    def test_game_detail_view(self):
        """A function for testing game's detail."""
        response = self.client.get(self.game.get_absolute_url())
        no_response = self.client.get("games/MU-Bayer/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Ajax-Real M")
        self.assertTemplateUsed(response, "games/game_detail.html")
