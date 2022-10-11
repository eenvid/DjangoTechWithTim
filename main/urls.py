from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name = 'home'),
    path("<int:id>", views.v1, name='index'),
    path("create/", views.create, name = 'create')
]