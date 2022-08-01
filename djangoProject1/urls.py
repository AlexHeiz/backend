from django.contrib import admin
from django.urls import path, include, reverse
from tasks.models import Task




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('myapi/', include('myapi.urls')),
]
