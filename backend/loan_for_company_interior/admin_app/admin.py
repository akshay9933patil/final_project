from django.contrib import admin
from .models import User, Defaulter

# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile']
admin.site.register(User, UserModelAdmin)        #admin.site.register(modelname)

admin.site.register(Defaulter)