from easyblog.image.models import Image, Gallery
from django.contrib import admin

class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal = ['images']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('inline_script',)

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)

