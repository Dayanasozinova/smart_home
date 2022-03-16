# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from smart_home.measurement.models import Sensor, Measurement
from smart_home.measurement.serializers import SensorDetailSerializer, MeasurementSerializer


class ListCreateAPIView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        result = SensorDetailSerializer(sensors, many=True)
        return Response(result.data)


class RetrieveUpdateAPIView(APIView):
    pass


class CreateAPIView(APIView):
    pass
