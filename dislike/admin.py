from django.contrib import admin
from dislike import models
# Register your models here.

@admin.register(models.DislikeModel)
class DisLikeAdmin(admin.ModelAdmin):
    list_display = ('disliker', 'product')
