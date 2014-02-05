from django.db import models

# Create your models here.
class Room(models.Model):
    password = models.CharField(max_length=200)
    def __unicode__(self):
        return "Room %d" % self.id

class Line(models.Model):
    room = models.ForeignKey(Room)
    text = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text
