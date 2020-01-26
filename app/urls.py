
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("login.urls")),
    path('caddy/', include("caddy.urls")),
    path('golfer/', include("golfer.urls")),
]
