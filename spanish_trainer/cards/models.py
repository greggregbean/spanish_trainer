from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    spanish_word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.spanish_word
