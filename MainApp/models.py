from django.db import models


# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100)


class Language(models.Model):
    name = models.CharField(max_length=100)


class LinkCountryLanguage(models.Model):
    id_country = models.PositiveIntegerField(default=0)
    id_language = models.PositiveIntegerField(default=0)
    name_country = models.CharField(max_length=100)  # временно
    name_language = models.CharField(max_length=100)  # временно

