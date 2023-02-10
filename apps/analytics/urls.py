from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.analytics.views import AnalyticListView

urlpatterns = [
    path('', AnalyticListView.as_view(), name="analytic-list"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
