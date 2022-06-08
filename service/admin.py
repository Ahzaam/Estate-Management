from django.contrib import admin
from . models import Feedback, Users, tempUser, AutoLoginToken

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Users)
admin.site.register(tempUser)
admin.site.register(AutoLoginToken)
