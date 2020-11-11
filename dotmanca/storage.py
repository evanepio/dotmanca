from django.conf import settings
from django.core.files.storage import FileSystemStorage
from storages.backends.s3boto3 import S3Boto3Storage


# From https://djangosnippets.org/snippets/976/
class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            self.delete(name)
        return name


class StaticStorage(S3Boto3Storage):
    location = settings.STATIC_LOCATION
    default_acl = "public-read"

    def size(self, name):
        """
        Return the total size, in bytes, of the file specified by name.
        """
        raise NotImplementedError("subclasses of Storage must provide a size() method")

    def get_accessed_time(self, name):
        """
        Return the last accessed time (as a datetime) of the file specified by
        name. The datetime will be timezone-aware if USE_TZ=True.
        """
        raise NotImplementedError(
            "subclasses of Storage must provide a get_accessed_time() method"
        )

    def get_created_time(self, name):
        """
        Return the creation time (as a datetime) of the file specified by name.
        The datetime will be timezone-aware if USE_TZ=True.
        """
        raise NotImplementedError(
            "subclasses of Storage must provide a get_created_time() method"
        )

    def get_modified_time(self, name):
        """
        Return the last modified time (as a datetime) of the file specified by
        name. The datetime will be timezone-aware if USE_TZ=True.
        """
        raise NotImplementedError(
            "subclasses of Storage must provide a get_modified_time() method"
        )


class PublicMediaStorage(S3Boto3Storage):
    location = settings.PUBLIC_MEDIA_LOCATION
    default_acl = "public-read"
    file_overwrite = True

    def size(self, name):
        """
        Return the total size, in bytes, of the file specified by name.
        """
        raise NotImplementedError("subclasses of Storage must provide a size() method")

    def get_accessed_time(self, name):
        """
        Return the last accessed time (as a datetime) of the file specified by
        name. The datetime will be timezone-aware if USE_TZ=True.
        """
        raise NotImplementedError(
            "subclasses of Storage must provide a get_accessed_time() method"
        )

    def get_created_time(self, name):
        """
        Return the creation time (as a datetime) of the file specified by name.
        The datetime will be timezone-aware if USE_TZ=True.
        """
        raise NotImplementedError(
            "subclasses of Storage must provide a get_created_time() method"
        )

    def get_modified_time(self, name):
        """
        Return the last modified time (as a datetime) of the file specified by
        name. The datetime will be timezone-aware if USE_TZ=True.
        """
        raise NotImplementedError(
            "subclasses of Storage must provide a get_modified_time() method"
        )
