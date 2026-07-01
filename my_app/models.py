from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self): return self.username

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()

    def __str__(self): return f"Букінг для {self.user.username} - {self.date} о {self.time}"

class Rooms(models.Model):
    rooms = []
    name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self): return self.name
