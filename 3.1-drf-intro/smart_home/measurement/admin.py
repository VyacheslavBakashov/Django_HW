from django.contrib import admin
from .models import Measurement, Sensor


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name', 'description']
    list_editable = ('name','description')


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor_id', 'measure', 'obtained_at', 'photo']
    search_fields = ['sensor_id', 'obtained_at']
    list_editable = ('measure', 'photo')
