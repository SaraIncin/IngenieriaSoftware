from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Song, Artist

from .forms import ArtistForm 

# Create your views here.
class Index(View):
    template = "index.html"
    def get(self,request):
        return render(request,self.template)

class ArtistView(View):
    """New Artist."""

    template = "registrar_artista.html"

    def get(self, request):
        """Render sign up form."""
        form = ArtistForm()
        contexto = {"form": form}
        return render(request, self.template, contexto)

    def post(self, request):
        """Receive and validate sign up form."""
        form = ArtistForm(request.POST)
        contexto = {"form": form}
        if not form.is_valid():
            return render(request, self.template, contexto)
        artista = Artist.objects.create(
        	name=form.cleaned_data["name"],
            image=form.cleaned_data["image"],
        )
        return redirect("principal")

        
class TopSongs(View):
    template = "topsongs.html"
    def get(self, request):
        """GET method."""
        songs = Song.objects.all()
        context = {"songs": songs}
        return render(request, self.template, context)
