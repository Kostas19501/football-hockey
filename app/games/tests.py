import datetime

from django.test import TestCase
from django.urls import reverse

from .models import Game


class GameTests(TestCase):
    """A class for testing the games app."""

    @classmethod
    def setUpTestData(cls):
        """A function for setting test data"""
        cls.game = Game.objects.create(
            title="ДИНАМО МОСКВА – ТОРПЕДО",
            description="| Обзор матча Фонбет КХЛ сезон 2024/2025 | 30.01.2025",
            data="2025-01-30",
            place="Dinamo Stadium",
            video="https://rutube.ru/play/embed/bcd058bb9b46c4a9e79e8a9c8158f7da",
            image="fghh.jpeg",
        )

    def test_game_listing(self):
        """Checks these all its string
        representation and content are correct."""
        self.assertEqual(f"{self.game.title}", "ДИНАМО МОСКВА – ТОРПЕДО")
        self.assertEqual(
            f"{self.game.description}",
            "| Обзор матча Фонбет КХЛ сезон 2024/2025 | 30.01.2025",
        )
        self.assertEqual(f"{self.game.data}", "2025-01-30")
        self.assertEqual(f"{self.game.place}", "Dinamo Stadium")
        self.assertEqual(
            f"{self.game.video}",
            "https://rutube.ru/play/embed/bcd058bb9b46c4a9e79e8a9c8158f7da",
        )
        self.assertEqual(f"{self.game.image}", "fghh.jpeg")

    def test_game_list_view(self):
        """
        Confirms that our main page returns the
        HTTP 200 status code, contains our text,
        displays creation date,
        and uses the correct one. games/game_list.html
        the template.
        """
        response = self.client.get(reverse("game_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "ДИНАМО МОСКВА – ТОРПЕДО")
        self.assertContains(response, "fghh.jpeg")
        self.assertContains(response, "30.01.2025")
        self.assertTemplateUsed(response, "games/game_list.html")

    def test_game_detail_view(self):
        """A function for testing game's detail."""
        response = self.client.get(self.game.get_absolute_url())
        no_response = self.client.get("games/MU-Bayer/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "ДИНАМО МОСКВА – ТОРПЕДО")
        self.assertContains(response, "fghh.jpeg")
        self.assertContains(
            response, "Турнир: | Обзор матча Фонбет КХЛ сезон 2024/2025 | 30.01.2025"
        )
        self.assertContains(response, "Дата: 30 Янв 2025")
        self.assertContains(response, "Стадион: Dinamo Stadium")
        self.assertContains(
            response, "https://rutube.ru/play/embed/bcd058bb9b46c4a9e79e8a9c8158f7da"
        )
        self.assertTemplateUsed(response, "games/game_detail.html")
