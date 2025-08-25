from django.db import models

class Token(models.Model):
    bio =  models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False)

    def __str__(self):
        return self.bio[:30] 