from django.db import models

# Create your models here.


class Feedback(models.Model):
    feebackid = models.AutoField(primary_key=True)
    feedback = models.CharField(max_length=50)
    viewed = models.BooleanField(default=False)
    def __str__(self):
            return self.feedback

class Users(models.Model):

    uuid = models.CharField(max_length=40)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=150)
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

class AutoLoginToken(models.Model):
    token = models.CharField(max_length=50)
    userid = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.token

class Licence(models.Model):
    accounts = [('Estate', 'estate'), ('Supplier', 'supplier'), ('Feildowner', 'feildowner'), ('Null', 'null')]
    userid = models.CharField(max_length=40, unique=True)
    acounttype = models.CharField(max_length=10, choices=accounts, default='Null')
    license = models.CharField(max_length=50, unique=True)
