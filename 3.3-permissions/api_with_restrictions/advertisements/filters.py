from django_filters import rest_framework as filters
from rest_framework.authtoken.admin import User

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateFromToRangeFilter()
    creator = filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status']