"""URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.users.urls', 'users'), namespace='users')),    
    path('', include(('apps.contacts.urls', 'contacts'), namespace='contacts')),    
    path('', include(('apps.tracking.urls', 'tracking'), namespace='tracking')),    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [

        path('__debug__/', include(debug_toolbar.urls)),
    ]
