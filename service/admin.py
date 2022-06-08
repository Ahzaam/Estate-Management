from django.contrib import admin
from . models import Feedback, Users, tempUser

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Users)
admin.site.register(tempUser)
