from django import forms
from .models import Album

class AlbumSearch(forms.Form):
    title_search = forms.CharField(max_length=100)    
    albums_searched = Album.objects.filter(title__icontains=title_search)