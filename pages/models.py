from django.db import models
from django.utils.text import slugify

class Pages(models.Model):
    title = models.CharField(max_length=255)  
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    text = models.TextField(default='')  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Details(models.Model):
    title = models.CharField(max_length=255)  
    page = models.ForeignKey(Pages, null=True, blank=True, on_delete=models.CASCADE, related_name='details')
    subtitle = models.CharField(max_length=255)
    text = models.TextField(default='') 
