from django.db import models
from certificates.models import Technology

from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class WorkExpirence(models.Model):
    title = CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name="all_technologies_workexpirence")
    image = ImageField(upload_to='portfolio/images')
    location = URLField(blank=True)
    initial_date = models.DateField(blank=True, null=True)
    final_date = models.DateField(blank=True, null=True)