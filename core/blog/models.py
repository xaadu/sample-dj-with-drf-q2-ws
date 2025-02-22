from django.db import models


class Post(models.Model):
    title = models.CharField()
    description = models.TextField()
    image = models.ImageField(upload_to="blog")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
