from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensors(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurements(models.Model):
    objects = None
    sensor_id = models.ForeignKey(Sensors, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_id = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'{self.sensor_id}: {self.temperature} in {self.created_id}'