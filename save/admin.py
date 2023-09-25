from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.SaveModel)
class SaveAdmin(admin.ModelAdmin):
    list_display = ('saver', 'product')
