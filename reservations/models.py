from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resevation for {self.user.username} on {self.date} at {self.time}"