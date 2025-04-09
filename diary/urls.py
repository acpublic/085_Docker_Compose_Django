from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView

app_name = "diary"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/", views.send, name="send"),
]