from django.urls import include, path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
    path('chas/', views.AboutChasView.as_view(), name='chas'),
    path('evan/', views.AboutEvanView.as_view(), name='evan'),
]
