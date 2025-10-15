from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Health check view
def healthz(request):
    return HttpResponse("OK")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('convert.urls')),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('healthz', healthz),  # <-- Render health check
]
