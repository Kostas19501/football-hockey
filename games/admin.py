from django.contrib import admin

from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "published_at",
    )


admin.site.register(Game, GameAdmin)
