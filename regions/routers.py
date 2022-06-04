from rest_framework import routers
from . import viewsets

router = routers.SimpleRouter()

router.register('region', viewsets.RegionViewSet)
router.register('city', viewsets.CityViewSet)

urlpatterns = router.urls
