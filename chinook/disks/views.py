from django.shortcuts import get_object_or_404, render

from .models import Track, Album, Artist


def index(request):
    albums = Album.objects.order_by("title")
    return render(request, "disks/index.html", {"albums": albums})


def details(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    tracks = Track.objects.filter(album=album_id)
    artist = album.artist.name
    return render(request, "disks/details.html", {"album": album.title, "tracks": tracks, "artist": artist})
