from django.urls import path
from django.contrib import admin

assert isinstance(path,object )
from django.urls import include, path

urlpatterns = [
    path('', include('myapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
