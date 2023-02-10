from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from .views import MyPasswordChangeView, MyPasswordSetView
from django.conf import settings  # add this
from django.conf.urls.static import static  # add this

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # WebsiteFront Template
                  path('', include('apps.front.urls')),
                  # Backend Users
                  path('dashboard/', include('apps.users.urls')),
                  # Dashboard
                  path('dashboard/', include('apps.dashboards.urls')),
                  path('dashboard/', include('apps.settings.urls')),
                  # Apps
                  path('dashboard/apps/', include('apps.applications.urls')),
                  # Layouts
                  path('dashboard/layouts/', include('apps.layouts.urls')),
                  # Components
                  path('dashboard/components/', include('apps.components.urls')),
                  # Pages
                  path('dashboard/pages/', include('apps.pages.urls')),
                  path(
                      "account/password/change/",
                      login_required(MyPasswordChangeView.as_view()),
                      name="account_change_password",
                  ),
                  path(
                      "account/password/set/",
                      login_required(MyPasswordSetView.as_view()),
                      name="account_set_password",
                  ),
                  # All Auth
                  # path('dashboard/account/', include('allauth.urls')),
                  # path('dashboard/social-auth/', include('social_django.urls', namespace="social")),


                  path('dashboard/services/', include('apps.services.urls')),
                  path('dashboard/products/', include('apps.products.urls')),
                  path('dashboard/services/', include('apps.services.urls')),

                  path('dashboard/menus/', include('apps.menus.urls')),
                  path('accounts/', include('apps.accounts.urls')),
                  path('analytics/', include('apps.analytics.urls')),

                  path('dashboard/groups/', include('apps.groups.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
