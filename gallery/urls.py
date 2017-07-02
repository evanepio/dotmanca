from django.conf.urls import url

from . import views

app_name = 'gallery'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', views.GalleryView.as_view(), name='gallery'),
    url(r'^(?P<gallery_slug>[-\w]+)/(?P<slug>[-\w]+)/$', views.GalleryImageView.as_view(), name='gallery_image'),
]
