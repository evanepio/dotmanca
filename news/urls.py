from django.urls import include, path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.ArticleView.as_view(), name='article'),
]
