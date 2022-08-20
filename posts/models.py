from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='author_images')
    caption = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    class Meta:
        # pakeičia įkeltų postų eiliškumą, kad paskutinis būtų atvaizduojamas pirmas
        ordering = ['-date_created'] 