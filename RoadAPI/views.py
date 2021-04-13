from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework import viewsets
from RoadAPI.models import Road, Point
from RoadAPI.serializers import RoadSerializer, PointSerializer


def index(request):
    return HttpResponse("API in development. Hopefully, something cool will be here soon.")


def json_test(request):
    data = {
        "message": "Hiya",
        "time": "still WIP"
    }
    return JsonResponse(data)


class RoadViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Roads
    """
    queryset = Road.objects.all()
    serializer_class = RoadSerializer


class PointViewSet(viewsets.ReadOnlyModelViewSet):
    """
    RO Endpoint for Points
    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer
