from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings

urlpatterns = [
    # REQUIRED --------------------------------------------------------- #
    path('admin/', admin.site.urls),
    path('accounts/', include('src.accounts.urls', namespace='accounts')),
    path('accounts/', include('allauth.urls')),

    # PORTALS ---------------------------------------------------------- #
    # path('', include('src.wsite.urls', namespace='wsite')),
    path('a/', include('src.portals.admins.urls', namespace='admins-portal')),
    path('c/', include('src.portals.customer.urls', namespace='customer-portal')),

    # DEPRECATED ------------------------------------------------------- #
    path('site/', include('src.wsite.urls', namespace='wsite')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
