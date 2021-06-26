from rest_framework import permissions,response,status
from rest_framework.generics import CreateAPIView
from . import serializers,models


class TireOrderAPIView(CreateAPIView):
    serializer_class = serializers.TireOrderSerializer
    permission_classes = [permissions.AllowAny]
    

class OilOrderAPIView(CreateAPIView):
    serializer_class = serializers.OilOrderSerializer
    permission_classes = [permissions.AllowAny]

    
