from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

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


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post")  # prevents duplicate likes

    def __str__(self):
        return f"{self.user.username} likes {self.post.id}"