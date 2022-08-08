from django.contrib import admin
from .models import Fines, Category


class FinesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'time_create', 'is_published')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Fines, FinesAdmin)
admin.site.register(Category, CategoryAdmin)
