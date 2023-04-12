from django.shortcuts import get_object_or_404, render

from .models import Track, Album, Artist


def index(request):
    albums=Album.objects.order_by("title")
    context = {"albums":albums}
    return render(request, "disks/index.html", context)


def details(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, "disks/details.html", {"album": album})
