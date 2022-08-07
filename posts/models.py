from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.caption

    class Meta:
        ordering = ['-date_created'] # pakeičia įkeltų postų eiliškumą, kad paskutinis būtų atvaizduojamas pirmas