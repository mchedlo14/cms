from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from apps.services.views import (ServiceListView,
                            ServiceCreateView,
                            ServiceDeleteView,
                            EditServiceView,
                            CategoryListView,
                            CategoryDeleteView,
                            EditCategoryView,
                            CategoryCreateView)

urlpatterns = [
                  path('', ServiceCreateView.as_view(), name="service-create"),
                  path('all/', ServiceListView.as_view(), name="service-list"),
                  path('edit/<int:id>', EditServiceView.as_view(), name="service-edit"),
                  path('delete/<int:id>', ServiceDeleteView.as_view(), name="service-delete"),
                  path('category/create/', CategoryCreateView.as_view(), name="service-category-create"),
                  path('category/all/', CategoryListView.as_view(), name="service-category-list"),
                  path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name="service-category-delete"),
                  path('category/edit/<slug:slug>/', EditCategoryView.as_view(), name="service-category-edit"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
