from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique="True")
    name = models.CharField(max_length=500)
    # avatar = models.ImageField(default='blankPhoto.jpg', blank=True, upload_to='profile_images')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
        
    #     img = Image.open(self.avatar.path)
        
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.avatar.path)


