from django.urls import path

from . import views

app_name = "search"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>",views.data, name="titles")
]
