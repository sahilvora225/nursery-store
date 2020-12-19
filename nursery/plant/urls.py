from django.urls import path, include

from rest_framework import routers

from .views import PlantView


app_name = 'plant'

router = routers.DefaultRouter()
router.register('', PlantView)

urlpatterns = [
    path('', include(router.urls)),
]
