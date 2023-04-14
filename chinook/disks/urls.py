from django.urls import path

from . import views
app_name="disks"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>/', views.details, name='details'),
    
    #default route at https://example.com:8000
    path('', views.index, name="home")
]