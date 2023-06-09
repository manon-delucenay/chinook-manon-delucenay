from django.db import models


class Artist(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Album(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


class Track(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    composer = models.CharField(max_length=200, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unitPrice = models.DecimalField(max_digits=5, decimal_places=2)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def duration(self):
        return round(self.milliseconds/60000,2)
