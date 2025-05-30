from django.db import models
from certificates.models import Technology

from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

# Create your models here.

class Projects(models.Model):
    title = CharField(max_length=100)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name="all_technologies_projects")
    image = ImageField(upload_to='portfolio/images/projects')
    url = URLField(blank=True)
    isPortfolio = models.BooleanField(default=False)

