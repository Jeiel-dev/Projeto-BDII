from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # colocar como login depois
    path('', include('login.urls'))
]
