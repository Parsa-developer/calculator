from django.db import models

# Create your models here.

class SaveData(models.Model):
    text = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.text)