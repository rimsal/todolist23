from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('todolist/', include('todo.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='todolist/', permanent=True)),
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))


