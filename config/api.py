from .models import Histoy
from rest_framework import viewsets, permissions
from .serializers import HistoySerializer

class HistoyViewSet(viewsets.ModelViewSet):
    queryset = Histoy.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = HistoySerializer