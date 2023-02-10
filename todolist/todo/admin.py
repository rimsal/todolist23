from django.contrib import admin
from .models import Uzduotis



class UzduotisAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'data',  'body')


admin.site.register(Uzduotis, UzduotisAdmin)

