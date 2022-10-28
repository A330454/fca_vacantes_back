from rest_framework.viewsets import mixins, GenericViewSet
from . import models
from . import serializers

# Create your views here.
class VacantesServicioViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset=models.Vacante.objects.all()
    serializer_class=serializers.VacanteServicioSerializer
    permission_classes=()