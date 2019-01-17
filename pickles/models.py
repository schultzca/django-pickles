from django.db import models


class PickleType(models.Model):
    name = models.CharField(max_length=50)


# Create your models here.
class Pickle(models.Model):
    pickle_type = models.ForeignKey(PickleType, on_delete=models.CASCADE)
    size = models.IntegerField()
    price = models.IntegerField()
