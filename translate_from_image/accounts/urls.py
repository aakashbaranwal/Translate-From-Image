from django.contrib import admin
from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'accounts'

urlpatterns = [

#    url(r'^login/', include('translate.urls', namespace='translate')),

]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))