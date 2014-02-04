from django.db import models

# Create your models here.
class Room(models.Model):
    def __unicode__(self):
        return "Room %d" % self.id

class Line(models.Model):
    room = models.ForeignKey(Room)
    text = models.CharField(max_length=500)

    def __unicode__(self):
        return self.text
