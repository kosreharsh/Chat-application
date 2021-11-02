from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)
    room_name = models.SlugField()

    def save(self, *args, **kwargs):
        self.room_name = slugify(self.name)
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(
        Room, related_name='messages', on_delete=models.CASCADE)
    handle = models.TextField(blank=True, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {handle}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')

    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
