from django.db import models
from django.utils.text import slugify

# Create your models here.
class Pages(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    text = models.CharField(max_length=100000, default='Default content')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


