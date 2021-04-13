from django.urls import path
from RoadAPI import views


urlpatterns = [
    path('', views.index, name="index"),
    path("jsonTest/", views.json_test, name="JsonDummy")
]
