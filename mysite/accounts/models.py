from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    icon = models.ImageField(upload_to = "image/", blank = True, null = True)
    message = models.TextField(blank = True, null = True)
    school = models.CharField(max_length = 20)

    def get_absolute_url(self):
        return reverse('sample: profile', kwargs = {'username': self.username})