from django.views.generic import ListView, DetailView

from .models import Game


class GameListView(ListView):
    """Представление для отображения списка матчей."""

    model = Game
    context_object_name = "game_list"
    template_name = "games/game_list.html"


class GameDetailView(DetailView):
    """A view to display the match."""

    model = Game
    context_object_name = "game"
    template_name = "games/game_detail.html"
