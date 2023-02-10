from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.products.views import (
    ProductListView,
    EditProductView,
    ProductDeleteView,
    CategoryCreateView,
    CategoryListView,
    CategoryDeleteView,
    EditCategoryView,
    ProductCreateView)

urlpatterns = [
                  path('create/', ProductCreateView.as_view(), name="product-create"),
                  path('all/', ProductListView.as_view(), name="product-list"),
                  path('edit/<slug:slug>/', EditProductView.as_view(), name="product-edit"),
                  path('delete/<slug:slug>/', ProductDeleteView.as_view(), name="product-delete"),
                  path('category/create/', CategoryCreateView.as_view(), name="product-category-create"),
                  path('category/all/', CategoryListView.as_view(), name="product-category-list"),
                  path('category/delete/<slug:slug>/', CategoryDeleteView.as_view(), name="product-category-delete"),
                  path('category/edit/<slug:slug>/', EditCategoryView.as_view(), name="product-category-edit"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
