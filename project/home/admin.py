from django.contrib import admin
from .models import Home

# Register your models here.

class homeAdmin(admin.ModelAdmin):
    list_display=['title','info']

admin.site.register(Home,homeAdmin)
