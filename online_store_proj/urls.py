from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #accounts
    path('accounts/', include('django.contrib.auth.urls')),
    
    #local apps
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
]