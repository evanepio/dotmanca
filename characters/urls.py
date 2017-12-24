from django.urls import path

from . import views

app_name = 'characters'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:team_slug>/<slug:slug>/', views.CharacterView.as_view(), name='character'),
]
