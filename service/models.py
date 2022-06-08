from django.db import models

# Create your models here.


class Feedback(models.Model):
    feedback = models.CharField(max_length=50)
    viewed = models.BooleanField(default=False)
    def __str__(self):
            return self.feedback

class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=40)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)

    def __str__(self):
        return self.email

class tempUser(models.Model):
    otp = models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=40)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)

    def __str__(self):
        return self.name
