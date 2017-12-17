from django.urls import include, path

from . import views

app_name = 'places'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.PlaceView.as_view(), name='place'),
]
