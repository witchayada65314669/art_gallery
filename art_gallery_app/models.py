from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
    artist_id = models.IntegerField()

    def __str__(self):
        return self.title