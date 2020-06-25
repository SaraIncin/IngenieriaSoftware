"""Users URL configuration."""
# Django
from django.contrib import admin
from django.urls import include, path

# Views
from . import views

urlpatterns = [
    path('top_songs/',views.TopSongs.as_view(),name='top_songs'),
    path("create-artist/", views.ArtistView.as_view(), name="registro_artista"),
]
