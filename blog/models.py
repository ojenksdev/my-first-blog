from django.conf import settings
from django.db import models
from tinymce import HTMLField
from django.utils import timezone


class Post(models.Model):
    """Represents the posts made by a blogger."""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = HTMLField('Text')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Used to publish posts to the website"""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Returns a string representation of the post title"""
        return self.title
