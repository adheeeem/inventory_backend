from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import *

class InventorySerializer(ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = '__all__'

class StoreSerializer(ModelSerializer):
    class Meta:
        model = StoreModel
        fields = '__all__'

class ActionSerializer(ModelSerializer):
    class Meta:
        model = ActionModel
        fields = '__all__'