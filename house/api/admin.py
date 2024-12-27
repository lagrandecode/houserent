from django.contrib import admin
from .models import Grid

# Register your models here.


@admin.register(Grid)
class GridAdmin(admin.ModelAdmin):
    list_display = ('name','address','price')