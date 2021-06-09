from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from . import serializers


class TireOrderAPIView(CreateAPIView):
    serializer_class = serializers.TireOrderSerializer
    permission_classes = [permissions.AllowAny]
    

class OilOrderAPIView(CreateAPIView):
    serializer_class = serializers.OilOrderSerializer
    permission_classes = [permissions.AllowAny]
    
