from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Producer
from .serializers import ProducerSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    
    permission_classes = [AllowAny]
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

    def get_queryset(self):
        return self.queryset