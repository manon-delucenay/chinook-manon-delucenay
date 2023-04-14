from django import forms

class AlbumSearch(forms.Form):
    title_search = forms.CharField(label="Album title contains",max_length=100)