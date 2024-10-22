from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Projects(models.Model):
    title = CharField(max_length=100)
    description = models.TextField()
    image = ImageField(upload_to='portfolio/images')
    url = URLField(blank=True)

