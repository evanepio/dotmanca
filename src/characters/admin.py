from django.contrib import admin

from .models import Character, Team

admin.site.register(Team)
admin.site.register(Character)
