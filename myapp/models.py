from django.db import models

class UserData(models.Model):
    name = models.CharField(max_length=255)  # Store the name
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return self.name
