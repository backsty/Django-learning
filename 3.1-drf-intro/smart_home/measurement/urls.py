from django.urls import path

from .views import SensorView, MeasurementView, MeasurementsSensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', SensorView.as_view()),
    path('sensor/<int:sensor_id>/', MeasurementsSensorView.as_view()),
    path('sensor/<int:sensor_id>/<str:sensor_description>/', SensorView.as_view()),
    path('sensor/<int:sensor_name>/<str:sensor_description>/', SensorView.as_view()),
    path('measurement/<int:sensor_id>/<str:temp_val>/', MeasurementView.as_view()),
]