from rest_framework import viewsets, status
from rest_framework.response import Response

from . import models, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action


class RegionViewSet(viewsets.ModelViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, url_path='cities')
    def cities_by_region(self, request, pk):
        instance = self.get_object()
        city_serializer = serializers.CitySerializer(instance.cities.all(), many=True)
        return Response(city_serializer.data, status=status.HTTP_200_OK)


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
