from django.urls import path

from . import views
app_name="disks"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.details, name='details'),
]