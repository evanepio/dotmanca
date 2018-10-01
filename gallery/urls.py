from django.urls import path

from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<slug:slug>/", views.GalleryView.as_view(), name="gallery"),
    path(
        "<slug:gallery_slug>/<slug:slug>/",
        views.GalleryImageView.as_view(),
        name="gallery_image",
    ),
]
