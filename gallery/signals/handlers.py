from django.db.models.signals import post_delete
from django.dispatch import receiver

from gallery.models import GalleryImage


@receiver(post_delete, sender=GalleryImage)
def delete_image_after_record_removal(sender, instance, **kwargs):
    instance.the_image.delete(save=False)
