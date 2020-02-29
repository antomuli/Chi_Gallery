from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.my_photos, name='myPhotos'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^category/(\d+)', views.get_category, name = 'get_category'),
    url(r'^location/(\d+)', views.get_location, name = 'get_location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)