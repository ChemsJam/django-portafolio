from django.db import models
from django.db.models.fields import CharField, URLField
import datetime
# Create your models here.

class Technology(models.Model):
    CATEGORY_CHOICES = [
        ('language', 'Lenguaje'),
        ('framework', 'Framework'),
        ('software', 'Software'),
        ('tool', 'Herramienta'),
        ('library', 'Librería'),
        ('other', 'Otro'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='portfolio/images/technologies',blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Certificate(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name="all_technologies")
    image = models.ImageField(upload_to='portfolio/images/certificates')
    date = models.DateField(default=datetime.date.today)
    url = URLField(blank=True)
    
    def __str__(self):
        return self.name