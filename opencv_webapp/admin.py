from django.contrib import admin
from .models import ImageUploadModel
# Register your models here.

#ref:) site_2 customizing !!
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('description','document',)

admin.site.register(ImageUploadModel, ImageUploadAdmin)
