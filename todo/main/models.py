from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favourite = models.BooleanField(default=False)

class ToMeet(models.Model):
    persone = models.TextField()
    phone_number = models.CharField(max_length=50)
    date_of_meeting = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


