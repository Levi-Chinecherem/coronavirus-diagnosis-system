# coronavirus_reporting_system/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diagnosis.urls')),
    path('accounts/', include('account.urls')),
]
