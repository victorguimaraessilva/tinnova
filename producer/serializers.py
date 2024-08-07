from rest_framework import serializers
from .models import Producer


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = (
            'id',
            'cultures',
            'document',
            'producer_name',
            'farm_name',
            'city',
            'state',
            'total_area',
            'arable_area',
            'vegetation_area',
            'created_at', 
            'updated_at', 
            'deleted_at'
        )

    def validate(self, data):
        if data['total_area'] < (data['arable_area'] + data['vegetation_area']):
            raise serializers.ValidationError(
                "A soma de área agrícultável e vegetação, não deverá ser maior que a área total da fazenda.'"
            )
        return data