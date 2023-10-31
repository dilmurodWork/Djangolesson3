from django.contrib import admin
from django.urls import path, include  # 4.1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))  # 4.2
]
