from rest_framework import serializers

from RoadAPI.models import Road, Point


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ['order', 'x_coord', 'y_coord']


class RoadSerializer(serializers.ModelSerializer):
    point = PointSerializer(many=True, source='point_set')

    class Meta:
        model = Road
        fields = ['id', 'name', 'city', 'state', 'point']

    def create(self, validated_data):
        point_data = validated_data.pop('point_set')
        road = Road.objects.create(**validated_data)
        for point_obj in point_data:
            Point.objects.create(road=road, **point_obj)
        return road
