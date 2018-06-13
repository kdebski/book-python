from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include(('contact.urls', 'contact'), namespace='contact')),
]