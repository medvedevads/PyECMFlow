from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from apps.accounts.views import login_view, profile_view
from apps.dashboard.views import dashboard
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(dashboard), name='dashboard'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/profile/', login_required(profile_view), name='profile'),
    path('', include(('apps.accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('apps.dashboard.urls', 'dashboard'), namespace='dashboard')),
    path('', include(('apps.business_partner.urls', 'business_partner'), namespace='business_partner')),
    path('', include(('apps.tasks.urls', 'tasks'), namespace='tasks')),
    path('', include(('apps.contracts.urls', 'contracts'), namespace='contracts')),
    path('', include(('apps.contact.urls', 'contact'), namespace='contact')),
    path('search/', include(('apps.search.urls', 'search'), namespace='search')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
