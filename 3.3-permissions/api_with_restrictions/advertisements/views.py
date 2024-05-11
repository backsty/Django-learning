from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer

from advertisements.permissions import IsOwnerReadOnly

from advertisements import filters

from advertisements.models import AdvertisementStatusChoices


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета, сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerReadOnly]
    filterset_class = filters.AdvertisementFilter

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.is_superuser = None

    def get_permissions(self):
        """Получение прав для действий."""
        if self.is_superuser:
            return [IsAuthenticated()]
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerReadOnly()]
        return []

    def get_queryset(self):
        """Фильтрация объявлений по статусу"""
        if self.request.user.is_siperuser:
            return Advertisement.objects.all()
        elif self.request.user.is_authenticated:
            queryset = Advertisement.objects.exclude(status=AdvertisementStatusChoices.DRAFT)
            drafts = Advertisement.objects.filter(creator=self.request.user, status=AdvertisementStatusChoices.DRAFT)
            return queryset | drafts