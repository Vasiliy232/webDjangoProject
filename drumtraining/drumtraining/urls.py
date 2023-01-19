from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('education.urls', namespace='education')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
