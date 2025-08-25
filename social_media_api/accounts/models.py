from django.db import models
from django.contrib.auth.models import AbstractUser

class Token(models.Model):
    bio =  models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.bio[:30] 