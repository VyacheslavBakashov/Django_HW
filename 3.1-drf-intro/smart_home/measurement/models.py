from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=100, blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Сенсор')
    measure = models.FloatField(verbose_name='Измерение')
    obtained_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время измерения')
    photo = models.ImageField(upload_to='photos', blank=True, verbose_name='Фото', null=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['-obtained_at', 'sensor_id']
