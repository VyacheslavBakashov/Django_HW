from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrAdmin, IsReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_queryset(self):
        """Статус объявления DRAFT доступен к показу только владельцу и админам"""
        user = self.request.user
        if user.is_superuser:
            return super().get_queryset()
        elif user.is_anonymous:
            return Advertisement.objects.all().exclude(status='DRAFT')
        elif user.is_authenticated:
            queryset_temp = Advertisement.objects.all().exclude(status='DRAFT')
            queryset_draft = Advertisement.objects.filter(status='DRAFT', creator=user)
            return queryset_temp | queryset_draft

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwnerOrAdmin()]
        return [IsReadOnly()]
