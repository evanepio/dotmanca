from django.urls import path

from . import views

app_name = 'comics'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/', views.IssueView.as_view(), name='issue'),
]
