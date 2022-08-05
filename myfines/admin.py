from django.contrib import admin
from .models import Fines


class FinesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time_create', 'is_published')


admin.site.register(Fines, FinesAdmin)


