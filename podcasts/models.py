from django.db import models


class Episode(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField()
    link = models.URLField()
    image = models.URLField()
    podcast_name = models.CharField(max_length=255)
    guid = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.podcast_name}: {self.title}"
