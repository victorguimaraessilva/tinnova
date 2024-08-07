from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Culture
from .serializers import CultureSerializer


class CultureViewSet(viewsets.ModelViewSet):
    
    permission_classes = [AllowAny]
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer

    def get_queryset(self):
        return self.queryset