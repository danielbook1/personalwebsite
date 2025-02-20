from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.subject