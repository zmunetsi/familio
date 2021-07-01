from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=200)
    origin = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
