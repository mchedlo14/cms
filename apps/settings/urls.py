from django.urls import path
from django.urls import path  
from django.conf import settings #add this
from django.conf.urls.static import static #add this
from django.conf import settings  
from apps.settings.views import (
    EditWebParametresView,

)

app_name = 'settings'


urlpatterns = [
    path('settings',EditWebParametresView.as_view(), name="web_settings"),
    path('settings/api',EditWebParametresView.as_view(),name="api"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)