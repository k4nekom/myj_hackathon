from django.db import models
from accounts.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(
        'accounts.User', on_delete = models.CASCADE,
    )
    title = models.CharField(
        max_length = 200,
    )
    text = models.TextField(

    )
    picture = models.ImageField(
        upload_to = "image/posts/",
        blank = True,
        null = True,
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        blank = True,
    )

class Comment(models.Model):
    author = models.ForeignKey(
        'accounts.User', on_delete = models.CASCADE,
    )

    post = models.ForeignKey(
        'posts.Post', on_delete = models.CASCADE,
    )

    text = models.TextField(
        blank = True,
    )

class Like(models.Model):
    author = models.ForeignKey(
        'accounts.User', on_delete = models.CASCADE,
    )

    post = models.ForeignKey(
        'posts.Post', on_delete = models.CASCADE,
    )