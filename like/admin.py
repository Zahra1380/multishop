from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.LikeModel)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('liker', 'product')