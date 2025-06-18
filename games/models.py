import uuid
from django.db import models
from django.urls import reverse


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.URLField(max_length=200)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("game_detail", args=[str(self.id)])
