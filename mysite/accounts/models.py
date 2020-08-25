from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    icon = models.ImageField(upload_to = "image/", blank = True, null = True)
    message = models.TextField(blank = True, null = True)
    twitter_url = models.URLField(max_length = 300, default='https://twitter.com/')

    def get_absolute_url(self):
        return reverse('sample: profile', kwargs = {'username': self.username})