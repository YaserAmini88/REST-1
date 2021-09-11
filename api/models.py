from django.db import models

class Sports(models.Model):
    name = models.CharField(max_length=20)
    sport = models.CharField(max_length=10)
    age = models.IntegerField()
    def __str__(self):
        return self.name