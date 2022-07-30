
from django.contrib import admin
from django.urls import path, include, reverse

'''
from tasks.views import TaskAPIView
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),

]
