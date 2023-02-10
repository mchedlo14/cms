from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.menus.views import *

urlpatterns = [
    path('', MenuCreateView.as_view(), name="menu-create"),
    path('all/', MenuListView.as_view(), name="menu-list"),
    path('edit/<int:id>', EditMenuView.as_view(), name="menu-edit"),
    path('delete/<int:id>', MenuDeleteView.as_view(), name="menu-delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
