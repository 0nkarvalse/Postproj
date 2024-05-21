from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WebPost(models.Model):
    name = models.CharField(max_length=100, blank=False)
    post_type = (
        ('post', 'Post'),
        ('reels', 'Reels')
    )
    post_type = models.CharField(max_length=5, choices=post_type, blank=True)
    image = models.ImageField(upload_to='images/', blank=False)
    image_alt = models.CharField(max_length=300, blank=True)
    url = models.URLField(blank=False)
    position = models.PositiveIntegerField()
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.name
