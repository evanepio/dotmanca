from django.db import models
from django.db.models.signals import post_init, post_save, post_delete
from django.dispatch import receiver
from django.urls import reverse


class Gallery(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    added_timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    sort_order = models.IntegerField()

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('gallery:gallery', kwargs=kwargs)

    def __str__(self):
        return self.name


def gallery_image_upload_to(instance, file_name):
    file_extension = file_name.split(".")[-1]
    return F'galleries/{instance.gallery.slug}/{instance.slug}.{file_extension}'


class GalleryImage(models.Model):
    gallery = models.ForeignKey(Gallery)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    sort_order = models.IntegerField()

    the_image = models.ImageField(null=False, blank=False, upload_to=gallery_image_upload_to)
    added_timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        kwargs = {'gallery_slug': self.gallery.slug, 'slug': self.slug}
        return reverse('gallery:gallery_image', kwargs=kwargs)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('gallery', 'slug')


@receiver(post_init, sender=GalleryImage)
def backup_image_path(sender, instance, **kwargs):
    instance._current_image_file = instance.the_image


@receiver(post_save, sender=GalleryImage)
def delete_old_image(sender, instance, **kwargs):
    if hasattr(instance, '_current_image_file'):
        if instance._current_image_file != instance.the_image.path:
            instance._current_image_file.delete(save=False)


@receiver(post_delete, sender=GalleryImage)
def delete_image_after_record_removal(sender, instance, **kwargs):
    instance._current_image_file.delete(save=False)
