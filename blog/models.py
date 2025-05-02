from django.db import models
import datetime
import os

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    imgs = models.ImageField(upload_to='blog/post_images')
    date = models.DateField(datetime.date.today)
    
class PostImage(models.Model):
    def post_image_upload_to(instance, filename):
        # Genera la ruta basada en el título del post
        post_title = instance.post.title.replace(" ", "_")  # Reemplaza espacios por guiones bajos
        return os.path.join(f'blog/images/post_images/{post_title}', filename)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=post_image_upload_to)
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.post.title}"