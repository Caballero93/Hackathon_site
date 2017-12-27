from django.db import models

# Create your models here.
class HallOfFame(models.Model):
    name = models.CharField(max_length=200)
    score = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['score']