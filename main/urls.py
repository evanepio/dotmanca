from django.conf.urls import url
from django.views import generic

from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.AboutView.as_view(), name='about'),
    url(r'^chas/$', views.AboutChasView.as_view(), name='chas'),
    url(r'^evan/$', views.AboutEvanView.as_view(), name='evan'),
]
