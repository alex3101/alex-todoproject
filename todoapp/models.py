from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.db.models import DateTimeField

# Create your models here.
class Todo(models.Model):
    STATUSES = (
        (0, 'Completed'),
        (1, 'Not Completed'),
    )
    title = models.CharField(max_length=100)
    deadline = models.DateTimeField()  #.strf(" %A, %d %B %Y, %H %M ")
    description = models.TextField()
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=0)
    user = User()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.CharField(max_length=50)                          #OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user

