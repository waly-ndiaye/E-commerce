
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('admin/', include('admin_volt.urls')), 
    path('', include('frontend.urls'))
]
