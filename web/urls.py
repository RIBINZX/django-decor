from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "web"

urlpatterns = [
    # path("", views.index, name="index"),
    # path("detail/<slug>", views.detail, name="detail"),
    path("", views.BookListView.as_view(), name="index"),
    path('detail/<slug>',views.BookDetailView.as_view(),name="detail"),
    path("addbook/",views.BookCreateView.as_view(),name='addbook')
]
