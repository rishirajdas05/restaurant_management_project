
from django.db import models

class Feedback(models.Model):
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # First 40 chars as a preview
        return (self.comment[:40] + "…") if len(self.comment) > 40 else self.comment