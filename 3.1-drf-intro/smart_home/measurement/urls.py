from django.urls import path
from measurement.views import SensorsList, SensorView, MeasurementCreate

urlpatterns = [

    path('sensors/', SensorsList.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementCreate.as_view()),

]

