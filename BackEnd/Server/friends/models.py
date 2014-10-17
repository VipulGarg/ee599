from django.db import models

class FriendsConnectivity(models.Model):
    name = models.CharField(max_length=100)
    idval = models.IntegerField(primary_key=True)
    size = models.IntegerField()
    listf = models.CommaSeparatedIntegerField(max_length=200)
