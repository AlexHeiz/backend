from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
urlpatterns = [
    path('tasks/<int:pk>/complete/', views.set_complete),
    path('', include(router.urls)),
]