from django.urls import path
from . import views
from django.urls.conf import URLPattern


class MyURLPattern(URLPattern):
    pass


urlpatterns = [
    path('', views.index, name='index'),
    path("form/", views.form),
]