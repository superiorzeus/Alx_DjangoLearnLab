from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actor")
    verb = models.CharField(max_length=255)  # e.g., "liked your post"
    target_ct = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    target_id = models.PositiveIntegerField(null=True, blank=True)
    target = GenericForeignKey("target_ct", "target_id")
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor} {self.verb} {self.target} -> {self.recipient}"