from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique="True")
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} profilis'

    # def save(self):
    #     super().save()
