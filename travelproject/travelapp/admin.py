from django.contrib import admin
from .models import place, teams

admin.site.register(place)

# Register your models here.
admin.site.register(teams)