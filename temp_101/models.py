from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    comments = []

    def get_url(self):
        return '/blog/update/1'

    def serialize(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description}
