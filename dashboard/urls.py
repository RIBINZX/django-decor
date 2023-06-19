from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "dashboard"

urlpatterns = [
    path("purple", views.purple, name="purple"),
    path("purples", views.PurpleListView.as_view(), name="purples"),
  
]