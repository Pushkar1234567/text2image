from django.db import models

class GeneratedImage(models.Model):
    text = models.CharField(max_length=255)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated Image for '{self.text}'"
