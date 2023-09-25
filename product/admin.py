from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.ProductSize)
admin.site.register(models.ProductColor)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'slug']
    prepopulated_fields = {'slug': ('title', )}


class ProductInformationAdmin(admin.StackedInline):
    model = models.ProductInformation


class ProductImagesAdmin(admin.StackedInline):
    model = models.ProductImages

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'likes_count')
    inlines = (ProductInformationAdmin,ProductImagesAdmin)

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'parent')

admin.site.register(models.Gender)
