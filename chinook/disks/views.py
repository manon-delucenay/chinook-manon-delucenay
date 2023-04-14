from django.shortcuts import get_object_or_404, render
from django.forms import modelformset_factory

from .models import Track, Album, Artist
from .forms import AlbumSearch


def index(request):
    albums = Album.objects.order_by("title")
    return render(request, "disks/index.html", {"albums": albums})


def details(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    tracks = Track.objects.filter(album=album_id)
    artist = album.artist.name
    return render(request, "disks/details.html", {"album": album.title, "tracks": tracks, "artist": artist})


def search_albums(request):
    if request.method == "GET":
        form = AlbumSearch()
    elif request.method == "POST":
        obj = get_object_or_404()
        form = AlbumSearch(request.POST)
        if form.is_valid():
            return  # redirect to url with searched albums
    return render(request, "html", {"forms": form})  # insérer à l'index ??
