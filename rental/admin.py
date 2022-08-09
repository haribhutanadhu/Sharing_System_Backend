from django.contrib import admin
from .models import cycle, sport, electronic

# Register your models here.
@admin.register(cycle)
@admin.register(sport)
@admin.register(electronic)

class cycleAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'name', 'email', 'contact','describe']

class sportAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'name', 'email','contact','describe']

class electronicAdmin(admin.ModelAdmin):
    list_diplay = ['id', 'name', 'email','contact','describe']
