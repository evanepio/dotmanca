from django.contrib import admin

from .models import Gallery, GalleryImage


class GalleryImageInline(admin.StackedInline):
    model = GalleryImage


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery
    inlines = [GalleryImageInline, ]


admin.site.register(Gallery, GalleryAdmin)
