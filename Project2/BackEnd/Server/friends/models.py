from django.db import models

class FriendsConnectivity(models.Model):
    name = models.CharField(max_length=100)
    idval = models.IntegerField(primary_key=True)
    size = models.IntegerField()
    listf = models.CommaSeparatedIntegerField(max_length=200)
	
class TimeData(models.Model):
    time = models.CharField(max_length=100)
    idval = models.IntegerField(primary_key=True)
    count = models.IntegerField()
	
class ModelData(models.Model):
    changeingrowthrate = models.FloatField()
    idval = models.IntegerField(primary_key=True)
    count = models.IntegerField()
	
class VennIntersectionData(models.Model):
    facebook = models.IntegerField()
    idval = models.IntegerField(primary_key=True)
    twitter = models.IntegerField()
    intersection = models.IntegerField()
	
