from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=250)
    status = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    time_created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

# Create your models here.
