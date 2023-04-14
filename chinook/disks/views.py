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
    if request.method == "POST":
        search=AlbumSearch(request.POST)
        if search.is_valid():
            title_search=search.cleaned_data()
            albums = Album.objects.filter(title__unaccent__icontains=title_search)
        else : albums = get_object_or_404(Album)
    else : 
        search=AlbumSearch()
        albums = get_object_or_404(Album)
    return render(request, "index.html", {"album": albums, "form":search})  # insérer à l'index ??


