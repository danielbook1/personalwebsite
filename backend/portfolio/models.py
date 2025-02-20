from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title