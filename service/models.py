from django.db import models

# Create your models here.


class Feedback(models.Model):
    feedback = models.CharField(max_length=50)
    viewed = models.BooleanField(default=False)
    def __str__(self):
            return self.feedback
