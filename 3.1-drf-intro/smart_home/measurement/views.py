from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, \
    SensorSerializerDetail, MeasureSerializerCreate


class SensorsList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializerDetail


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MeasurementSerializer
        return MeasureSerializerCreate
