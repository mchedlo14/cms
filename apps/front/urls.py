from django.urls import path
from apps.front.views import (
    front_homepage,
    front_service,

)

app_name = 'front'

urlpatterns = [
    path('',view =front_homepage,name="homepage"),
    path('service',view =front_service,name="service"),
]