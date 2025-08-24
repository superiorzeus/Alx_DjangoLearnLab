from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    # Self-referential ManyToMany field for following
    following = models.ManyToManyField(
        'self',
        symmetrical=False,  # means A following B ≠ B following A
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username