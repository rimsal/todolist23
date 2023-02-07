from django.contrib import admin
from .models import Uzduotis


# Register your models here.

class UzduotisAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Uzduotis, UzduotisAdmin)

